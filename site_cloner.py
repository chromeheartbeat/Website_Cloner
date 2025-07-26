import os
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import requests
from pathlib import Path

visited_pages = set()
asset_cache = {}

def sanitize_filename(url):
    parsed = urlparse(url)
    path = parsed.path
    if path.endswith("/") or path == "":
        path += "index.html"
    return os.path.join(parsed.netloc, path.lstrip("/"))

def ensure_folder(path):
    Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)

def download_asset(url, base_dir):
    if url in asset_cache:
        return asset_cache[url]

    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        local_path = os.path.join(base_dir, sanitize_filename(url))
        ensure_folder(local_path)

        with open(local_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        rel_path = os.path.relpath(local_path, base_dir)
        asset_cache[url] = rel_path
        return rel_path
    except Exception as e:
        print(f"[!] Failed to download asset {url}: {e}")
        return None

def is_internal_link(link, domain):
    parsed = urlparse(link)
    return (not parsed.netloc or parsed.netloc == domain)

def rewrite_assets(soup, base_url, base_dir):
    tags_attrs = {
        "img": "src",
        "link": "href",
        "script": "src"
    }

    for tag, attr in tags_attrs.items():
        for el in soup.find_all(tag):
            file_url = el.get(attr)
            if not file_url or file_url.startswith(("data:", "#")):
                continue

            full_url = urljoin(base_url, file_url)
            local_file = download_asset(full_url, base_dir)
            if local_file:
                el[attr] = local_file

def clone_page(driver, url, base_dir, domain):
    if url in visited_pages:
        return
    visited_pages.add(url)

    print(f"[*] Visiting {url}")
    try:
        driver.get(url)

        driver.implicitly_wait(10)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        rewrite_assets(soup, url, base_dir)

        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            full_url = urljoin(url, href)
            if is_internal_link(full_url, domain):
                local_path = sanitize_filename(full_url)
                a_tag["href"] = local_path
                clone_page(driver, full_url, base_dir, domain)

        save_path = os.path.join(base_dir, sanitize_filename(url))
        ensure_folder(save_path)
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(soup.prettify())

    except Exception as e:
        print(f"[!] Failed to clone {url}: {e}")

def clone_website(url, output_dir="cloned_selenium_site"):
    options = uc.ChromeOptions()
    options.add_argument("--window-size=1280,800")

    driver = uc.Chrome(options=options)

    try:
        parsed = urlparse(url)
        domain = parsed.netloc
        os.makedirs(output_dir, exist_ok=True)

        print("[*] Opening the page in browser. Please solve captcha manually.")
        driver.get(url)

        input("Press Enter after you finish solving the captcha and page fully loads...")

        clone_page(driver, url, output_dir, domain)
        print("\n✅ Done! Site saved to:", output_dir)
    finally:
        driver.quit()

if __name__ == "__main__":
    clone_website("https://example.com")
