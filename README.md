# 🌐 Website_Cloner

A powerful Python tool to **recursively clone websites** using **Selenium** with `undetected-chromedriver`. Designed to bypass basic bot protections like **Cloudflare challenges**, it allows manual CAPTCHA solving and saves pages and assets for **offline browsing**.

---

## 🚀 Features

- 🕵️‍♂️ Uses `undetected-chromedriver` to evade bot detection
- 🧠 Opens a real Chrome browser to manually solve CAPTCHAs
- 🔄 Recursively clones pages within the same domain
- 🎨 Downloads all assets (images, CSS, JS)
- 🔗 Rewrites internal links for seamless offline browsing

---

## 📦 Requirements

- **Python** 3.8+
- **Google Chrome** (latest version)
- Python Packages:
  - `undetected-chromedriver`
  - `requests`
  - `beautifulsoup4`
  - `webdriver-manager`

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/chromeheartbeat/Website_Cloner.git
cd Website_Cloner

2. (Optional) Create and activate a virtual environment
Linux/macOS:

bash

python3 -m venv .venv
source .venv/bin/activate


3. Install dependencies
Using requirements file:

pip install -r requirements.txt

Or install individually:
pip install undetected-chromedriver requests beautifulsoup4 webdriver-manager

🧪 Usage

python site_cloner.py

A Chrome browser will open and load the target website.

If a CAPTCHA appears, solve it manually.

Return to the terminal and press Enter to continue.

The website will be saved to the cloned_selenium_site folder.

⚙️ Customization
Change target URL:
Edit this line in site_cloner.py:
clone_website("https://example.com")

Modify behavior:
Adjust cloning depth, asset filters, or custom rules directly in the script.

💡 Troubleshooting
✅ Ensure Google Chrome is installed and updated.

⚠️ Update undetected-chromedriver if you encounter driver errors:

bash

pip install --upgrade undetected-chromedriver
🔐 For persistent CAPTCHAs, consider:

Using residential proxies

Emulating real browser profiles
