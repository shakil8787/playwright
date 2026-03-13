

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    all_links = page.locator("a").all()
    for link in all_links:
        print(link.text_content(), "->", link.get_attribute("href"))
    browser.close()

