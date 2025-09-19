import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright,user_email,user_password,topic) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=10)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.kaggle.com/")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("button", name="Sign in with Email").click()
    page.get_by_role("textbox", name="Email / Username").click()
    page.get_by_role("textbox", name="Email / Username").fill(user_email)
    page.get_by_role("textbox", name="Email / Username").press("Tab")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(user_password)
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("link", name="Datasets", exact=True).click()
    page.get_by_role("textbox", name="Search datasets").click()
    page.get_by_role("textbox", name="Search datasets").fill(topic)
    # print(page.locator("a", has_text=topic))
    page.locator("a", has_text=topic).nth(1).click()
    page.get_by_text("file_downloadDownload").click()
    with page.expect_download() as download_info:
        page.get_by_text("Download dataset as zip").click()
    download = download_info.value
    path = f"dataset/{topic}.zip"
    download.save_as(path)
    
    context.close()
    browser.close()
    return path

def scrapper(user_email,user_password,topic):
    with sync_playwright() as playwright:
        path = run(playwright, user_email, user_password, topic)
    return path