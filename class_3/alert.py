from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # ব্রাউজার লঞ্চ করা
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # টার্গেট ইউআরএল-এ যাওয়া
    page.goto("https://www.tutorialspoint.com/selenium/practice/alerts.php")

    # page.on("dialog", lambda d: d.accept())
    # page.click("button[onclick='showAlert()']")

    # ডায়ালগ হ্যান্ডলার ফাংশন
    def handle_dialog(dialog):
        print(f"Dialog type: {dialog.type}")  # dialog.type ব্যবহার করা ভালো
        print(f"Dialog message: {dialog.message}")  # dialog.message ব্যবহার করা সঠিক পদ্ধতি
        dialog.dismiss()  # অ্যালার্ট 'OK' ক্লিক করা


    # ইভেন্ট লিসেনার সেট করা (বাটনে ক্লিকের আগেই এটি করতে হয়)
    page.on("dialog", handle_dialog)
    #
    # # কনফার্মেশন বক্স ট্রিগার করে এমন বাটনে ক্লিক
    # # 'myDesk()' ফাংশনটি একটি কনফার্মেশন বক্স ওপেন করে
    page.click("button[onclick='myDesk()']")

    # ফলাফল দেখার জন্য ৩ সেকেন্ড অপেক্ষা করুন (অপশনাল)
    page.wait_for_timeout(3000)

    # ব্রাউজার বন্ধ করা
    browser.close()