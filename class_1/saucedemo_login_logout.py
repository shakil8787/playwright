from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user", timeout=3000)
    page.locator("#password").fill("secret_sauce", timeout=3000)
    page.locator("#login-button").click()
    sleep(3)
    page.click("#react-burger-menu-btn")
    sleep(3)
    page.click("#logout_sidebar_link")
    sleep(3)
    browser.close()