from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://techcraftinator.weebly.com")
    driver.quit()

def main():
    test_selenium()

if __name__ == "__main__":
    main()