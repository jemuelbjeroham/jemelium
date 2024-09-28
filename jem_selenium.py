from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://techcraftinator.weebly.com")
    driver.get("https://techcraftinator.weebly.com/about.html")
    driver.back()
    driver.forward()
    input("Press enter to close the browser... ")
    # driver.quit()

def main():
    test_selenium()

if __name__ == "__main__":
    main()