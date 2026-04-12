from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/scroll-down.php")
    page.wait_for_timeout(3000)
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    #page.evaluate("window.scrollTo(0, 600)")
    page.wait_for_timeout(3000)
    page.close()