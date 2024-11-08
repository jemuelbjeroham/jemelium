# main_script.py
import getpass
from playwright.sync_api import sync_playwright
from playwright_script import run

# Gather data
device_data = {
    "serial_number": "12345ABC",
    "model_number": "XYZ-789",
    # Add other device data as needed
}

# Get username and password for login
username = input("Please enter your username: ")
password = getpass.getpass("Please enter your password: ")

# Run the Playwright script with the gathered data
with sync_playwright() as playwright:
    run(playwright, username, password, device_data)
