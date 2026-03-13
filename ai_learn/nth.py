from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    # সব লিঙ্কের মধ্যে দ্বিতীয় লিঙ্ক নির্বাচন করা (index 1)
    second_link = page.locator("a").nth(1)

    # লিঙ্কের টেক্সট ও href প্রিন্ট করা
    print("Text:", second_link.inner_text())
    print("URL:", second_link.get_attribute("href"))

    browser.close()