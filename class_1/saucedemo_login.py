from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("//input[@id='password']", "secret_sauce")
    sleep(3)
    page.click("#login-button")
    sleep(3)
    browser.close()