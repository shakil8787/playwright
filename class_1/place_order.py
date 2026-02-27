from time import sleep

from playwright.sync_api import playwright, sync_playwright

with sync_playwright() as shakil:
    browser = shakil.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("//input[@id='password']", "secret_sauce")
    sleep(3)
    page.click("#login-button")
    sleep(3)
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    sleep(3)
    page.click("#checkout")
    sleep(3)
    page.fill("#first-name", "shakil")
    page.fill("#last-name", "khan")
    page.fill("#postal-code", "6700")
    sleep(3)
    page.click("#continue")
    page.click("#finish")
    sleep(3)
    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")
    sleep(3)