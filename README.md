# Website_Cloner

A Python tool to recursively clone websites using Selenium with undetected-chromedriver, designed to bypass basic bot detection like Cloudflare challenges by enabling manual captcha solving. It downloads pages, assets (images, scripts, styles), and rewrites internal links for offline browsing.

Features
Uses undetected-chromedriver to reduce detection by bot protections

Opens a real Chrome browser for manual captcha solving

Recursively clones pages within the same domain

Downloads linked assets (images, CSS, JS)

Rewrites URLs for local browsing

Requirements
Python 3.8 or higher

Google Chrome browser installed

Packages below

Installation
Clone or download this repository.

(Optional but recommended) Create a virtual environment:

bash

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows PowerShell
Install required packages:

bash

pip install -r requirements.txt
Or install individually:

bash

pip install undetected-chromedriver requests beautifulsoup4 webdriver-manager
Usage
Run the script with Python:

bash

python site_cloner.py
A Chrome browser window will open and load the target website.

If a CAPTCHA appears, please solve it manually in the browser window.

After you finish, return to the console and press Enter to continue cloning.

The site will be saved in the cloned_selenium_site folder.

Notes
This tool is for educational purposes only.

Do not use it to clone or scrape websites without permission.

The author is not responsible for any misuse or legal consequences resulting from improper use.

Be respectful of website terms of service and copyright laws.

Customize
Change the URL to clone by editing the clone_website("https://example.com") line in site_cloner.py.

Adjust cloning depth or asset types by modifying the script.

Troubleshooting
Make sure Google Chrome is installed and updated.

If you encounter errors with ChromeDriver, ensure your undetected-chromedriver package is up to date.

If captchas persist, consider using residential proxies or advanced browser profiles.
