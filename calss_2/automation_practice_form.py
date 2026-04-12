from time import sleep

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    page.fill("#name", "john")
    page.fill("#email", "john@hero.com")
    page.click("#gender")
    sleep(1)
    page.click("#gender")
    sleep(1)
    page.fill("#mobile", "0123456789")
    page.fill("#dob", "1998-06-15") # Select year by value

    page.fill("#subjects", "quality assurance")
    page.click("#hobbies")
    sleep(1)
    page.set_input_files("//input[@id='picture']", "image/screenshot.png")
    page.fill("//textarea[@id='picture']","simple testing textarea")
    page.select_option("#state", index=2)
    sleep(1)
    page.select_option("#city", index=1)
    sleep(1)
    page.screenshot(path="image/screenshot.png")
    page.close()
    # page.click("input[value='Login']")