from time import sleep

from playwright.sync_api import sync_playwright, Dialog

def handle_dialog(dialog: Dialog):
    print(f" type: {dialog.type}")
    print(f" message: {dialog.message}")

    if dialog.type == "alert":
        dialog.accept()

    elif dialog.type == "confirm":
        # dialog.accept()
        dialog.dismiss()

    elif dialog.type == "prompt":
        dialog.accept("This is a prompt response")
        print(dialog.message)
        # dialog.dismiss()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.on("dialog", handle_dialog)

        page.goto("https://www.tutorialspoint.com/selenium/practice/alerts.php")
        page.click("button[onclick='showAlert()']")

        sleep(3)

        page.click("button[onclick='myDesk()']")

        sleep(3)
        page.click("button[onclick='myPromp()']")

        browser.close()