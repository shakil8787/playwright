# saucedemo login and logout using playwright with sync API
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("//input[@id='password']", "secret_sauce")
    page.click("#login-button")
    page.click("#react-burger-menu-btn")
    page.wait_for_selector("#logout_sidebar_link")
    page.click("#logout_sidebar_link")
    browser.close()
