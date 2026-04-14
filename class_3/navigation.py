from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.youtube.com/")
    print(page.title())
    page.goto("https://www.facebook.com/")
    page.wait_for_url("https://www.facebook.com/")
    sleep(3)
    page.go_back()
    sleep(3)
    page.go_forward()
    sleep(3)
    page.reload()
    sleep(3)

    browser.close()