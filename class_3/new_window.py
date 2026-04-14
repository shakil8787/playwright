from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context1 = browser.new_context()

    page1 = context1.new_page()
    page1.goto("https://www.google.com")

    #open second window
    context2 = browser.new_context()

    page2 = context2.new_page()
    page2.goto("https://www.github.com")
    page2.close()

    browser.close()