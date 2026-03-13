from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user", timeout=3000)
    page.locator("#password").fill("secret_sauce", timeout=3000)

    attribute_value = page.locator("#login-button").get_attribute("value")
    print(attribute_value)
    class_value = page.locator("#login-button").get_attribute("class")
    print(class_value)
    page.locator("#login-button").click()
    sleep(3)
    txt = page.locator("a[id='item_4_title_link'] div[class='inventory_item_name ']").text_content()
    print(txt)

    all_lacator = page.locator("div[class='inventory_item_name ']").all()
    for locator in all_lacator:
        print(locator.text_content())



    page.close()