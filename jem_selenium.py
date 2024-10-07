from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getpass

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.arista.com/en/login")
    # driver.get("https://techcraftinator.weebly.com/about.html")
    arista_username = driver.find_element(By.ID, "username")
    arista_username.send_keys("jemueljeroham.b@hcltech.com")
    arista_username.send_keys(Keys.RETURN)
    password = getpass.getpass("Enter the Support Portal Password: ")
    arista_password = driver.find_element(By.ID, "password")
    arista_password.send_keys(password)
    arista_password.send_keys(Keys.RETURN)

    # driver.back()
    # driver.forward()
    input("Press enter to close the browser... ")
    # driver.quit()

def main():
    test_selenium()

if __name__ == "__main__":
    main()