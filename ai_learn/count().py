from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    # সব লিঙ্কের সংখ্যা বের করা
    link_count = page.locator("a").count()
    print(f"মোট লিঙ্ক পাওয়া গেছে: {link_count}")

    # সব প্যারাগ্রাফের সংখ্যা বের করা
    paragraph_count = page.locator("p").count()
    print(f"মোট প্যারাগ্রাফ পাওয়া গেছে: {paragraph_count}")

    browser.close()