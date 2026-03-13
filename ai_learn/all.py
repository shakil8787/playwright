from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    # সব লিঙ্ক খুঁজে বের করা
    links = page.locator("a").all()

    # প্রতিটি লিঙ্কের টেক্সট ও href প্রিন্ট করা
    for link in links:
        text = link.inner_text()
        href = link.get_attribute("href")
        print(f"Text: {text} | URL: {href}")

    browser.close()