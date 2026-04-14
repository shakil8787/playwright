from time import sleep
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    # Create context properly
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.tutorialspoint.com/selenium/practice/browser-windows.php")

    # Wait for new tab
    with context.expect_page() as newtabinfo:
        page.click("button[title='New Tab']")

    newtab = newtabinfo.value
    newtab.wait_for_load_state()

    print("New tab title:", newtab.title())
    print("New tab url:", newtab.url)

    # Get all links
    all_links = newtab.locator("a").all()
    for link in all_links:
        print(link.get_attribute("href"))

    sleep(3)
    browser.close()