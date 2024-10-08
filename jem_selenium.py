from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass

def test_selenium():
    username = input("Enter your username: ")

    # Start the web driver (Chrome)
    driver = webdriver.Chrome()

    try:
        # Open the Arista login page
        driver.get("https://arista.my.site.com/AristaCommunity/s/support")

        # Wait for the username field to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        
        # Fill in the username
        arista_username = driver.find_element(By.ID, "username")
        arista_username.send_keys(username)
        arista_username.send_keys(Keys.RETURN)

        # Wait for the login type button to be present
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnLoginWired"))
        )

        # Click the login type button
        arista_lgntype = driver.find_element(By.ID, "btnLoginWired")
        arista_lgntype.click()

        # Securely prompt for the password
        password = getpass.getpass("Enter the Support Portal Password: ")

        # Wait for the password field to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )

        # Fill in the password
        arista_password = driver.find_element(By.ID, "password")
        arista_password.send_keys(password)
        arista_password.send_keys(Keys.RETURN)

        # Wait for login process to complete
        WebDriverWait(driver, 10).until(
            EC.url_changes("https://arista.my.site.com/AristaCommunity/s/support")
        )

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "New"))
        )

        # Click the New Case button
        arista_lgntype = driver.find_element(By.NAME, "New")
        arista_lgntype.click()

        # print("Login successful!")



    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Prompt the user before closing the browser
        input("Press enter to close the browser... ")
        driver.quit()

def main():
    test_selenium()

if __name__ == "__main__":
    main()
