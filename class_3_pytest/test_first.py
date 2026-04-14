from playwright.sync_api import sync_playwright
def test_first_case_1():
    assert 2+3==6

def test_first_case_2():
    assert 2+3!=6

def test_page_title():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.tutorialspoint.com/selenium/practice/alerts.php")
        print(page.title())
        assert page.title() == "Selenium Practice - Alerts"
        browser.close()

