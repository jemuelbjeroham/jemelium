import re
import getpass
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    username = input("Please enter your username: ")
    password = getpass.getpass("Please enter your password: ")
    page = context.new_page()
    page.goto("https://arista.my.site.com/AristaCommunity/s/support")
    page.goto("https://www.arista.com/en/login")
    page.locator("#username").click()
    page.locator("#username").click()
    page.locator("#username").fill(username)
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Arista Portal").click()
    page.locator("#password").click()
    page.locator("#password").fill(password)
    page.get_by_role("button", name="Login").click()
    page.goto("https://arista.my.site.com/AristaCommunity/secur/frontdoor.jsp?sid=00DA0000000H7UG%21AQEAQNS6gdl2ZaI7vf5b6Pk9BuvewRI4YzwpNB5KfmyTJn5WN2tduuD_ZkXvp92VbKpEXIIOPTbfDvPGWKQDejlDflDcoOXi&retURL=https%3A%2F%2Farista.my.site.com%2FAristaCommunity%2Fs%2Fsupport&loginURL=https%3A%2F%2Fsaml.salesforce.com%3Fssostartpage%3Dhttps%253A%252F%252Farista-ext.onelogin.com%252Ftrust%252Fsaml2%252Fhttp-post%252Fsso%252F318ef005-1ad9-488e-a384-c266260fb927%26saml_request_id%3D_2CAAAAZMENE-wMDAwMDAwMDAwMDAwMDAwAAAA-oqUl3KXg5PkO0fZ3rGwTA47kDuD1MvkBxnnfezZ0kQpWRjr-Ah4-Sq-_9qOw0uV9GYeRxo531GtyWQQ6Ew0SXKJCUT_El0m5-nf_dHBoJQQDoVNMMhyB64mt1GGh1FSvKF3SlmA3aw2t8yab3kSyNX4n0lRsf2TImKwG9bUqN8XIERCOR9o38yU3JtEl4vgpP7QiP7X3fdAF5ivdqsu8Iqm9wW2FUpmT2UcLjdUm-C6FOXsccBOrKiqrbDANyawKw%26logouturl%3Dhttps%253A%252F%252Faristanetworks.force.com%252FAristaCommunity%252Fs&cshc=w000008HvRt0000000H7UG")
    page.goto("https://arista.my.site.com/AristaCommunity/s/support")
    page.get_by_role("button", name="New Case").click()
    page.get_by_label("Priority").select_option("P4")
    page.get_by_label("*Subject").click()
    page.get_by_label("*Subject").fill("AUTOMATION TEST CASE - PLEASE DISREGARD")
    page.get_by_label("*HW Category").select_option("Data Center Products")
    page.get_by_label("Description").click()
    page.get_by_label("Description").click()
    page.get_by_role("button", name="Create Case").click()
    page.locator("#fileModalBody").get_by_role("button", name="Close").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
