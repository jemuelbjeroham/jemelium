import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass

logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG to capture all messages
                    format='%(asctime)s - %(levelname)s - %(message)s')

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

        logging.info("Waiting for any loading spinner to disappear.")

        WebDriverWait(driver, 20).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "slds-spinner_container"))
        )

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "New"))
        )

        # Click the New Case button
        arista_newcasebutton = driver.find_element(By.NAME, "New")
        arista_newcasebutton.click()

        # logging.info("Waiting for any loading spinner to disappear.")

        # WebDriverWait(driver, 20).until(
        #     EC.invisibility_of_element_located((By.CLASS_NAME, "slds-spinner_container"))
        # )

        # WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "slds-modal__container"))
        # )

        # # # print("Login successful!")

        # WebDriverWait(driver, 20).until(
        #     EC.invisibility_of_element_located((By.CLASS_NAME, "slds-spinner_container"))
        # )

        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "input-65"))
        # )
        logging.info("Waiting for the CC emails input field to be available.")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "input-65"))
        )
        # Fill the cc email ID
        arista_cc_email = driver.find_element(By.ID, "input-65")
        # arista_cc_email.click()
        driver.execute_script("arguments[0].scrollIntoView(true);", arista_cc_email)
        arista_cc_email.click()
        arista_cc_email.send_keys("testemail@jemtech.com")
        print(arista_cc_email.is_displayed())
        print(arista_cc_email.is_enabled())


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
