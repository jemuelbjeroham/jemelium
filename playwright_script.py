# playwright_script.py
import getpass
from playwright.sync_api import Playwright

def run(playwright: Playwright, username: str, password: str, device_data: dict) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Login
    page.goto("https://arista.my.site.com/AristaCommunity/s/support")
    page.goto("https://www.arista.com/en/login")
    page.locator("#username").fill(username)
    page.get_by_role("button", name="Continue").click()
    page.locator("#password").fill(password)
    page.get_by_role("button", name="Login").click()

    # Fill form with device data
    page.goto("https://arista.my.site.com/AristaCommunity/s/support")
    page.get_by_role("button", name="New Case").click()
    page.get_by_label("Priority").select_option("P4")
    page.get_by_label("*Subject").fill(f"Device Issue - {device_data['serial_number']}")
    page.get_by_label("*HW Category").select_option("Data Center Products")
    page.get_by_label("Description").fill(f"Model: {device_data['model_number']} - Automated Case Creation")
    page.get_by_role("button", name="Create Case").click()
    
    # Close modal and browser
    page.locator("#fileModalBody").get_by_role("button", name="Close").click()
    context.close()
    browser.close()
