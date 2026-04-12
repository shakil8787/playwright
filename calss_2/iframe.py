from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/frames.php")
    #normal text
    print(page.locator("//h2[normalize-space()='Iframe 1']").text_content())
    #iframe txt
    fremetxt = page.frame_locator("iframe[src='new-tab-sample.php']").first.locator("a[title='back to Selenium Tutorial']").text_content()
    print(fremetxt)

    page.close()