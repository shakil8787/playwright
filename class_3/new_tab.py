from playwright.sync_api import sync_playwright

with sync_playwright() as s:
    browser = s.chromium.launch(headless=False)
    context = browser.new_context()

    page1 = context.new_page()
    page1.goto("https://www.google.com")

    page2 = context.new_page()
    page2.goto("https://www.facebook.com")

    print("tab1:", page1.title())
    print("tab2:", page2.title())

    page1.bring_to_front()
    urls = page1.locator("a").all()
    for url in urls:
        print(url.get_attribute("href"))

    page2.bring_to_front()
    urls = page2.locator("a").all()
    for url in urls:
        print(url.get_attribute("href"))
    browser.close()