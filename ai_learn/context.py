from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 1️⃣ Browser launch
    browser = p.chromium.launch(headless=False)

    # 2️⃣ First Context (Admin Session)
    admin_context = browser.new_context()
    admin_page = admin_context.new_page()
    admin_page.goto("https://www.saucedemo.com/")
    admin_page.fill("#user-name", "standard_user")
    admin_page.fill("//input[@id='password']", "secret_sauce")
    admin_page.click("#login-button")

    # 3️⃣ Second Context (Normal User Session)
    user_context = browser.new_context()
    user_page = user_context.new_page()
    user_page.goto("https://www.saucedemo.com/")
    user_page.fill("#user-name", "standard_user")
    user_page.fill("//input[@id='password']", "secret_sauce")
    user_page.click("#login-button")

    # 4️⃣ Wait to observe
    admin_page.wait_for_timeout(5000)

    browser.close()