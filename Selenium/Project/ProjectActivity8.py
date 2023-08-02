from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Set up the Firefox Driver with WebDriverManger
service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:

    # Open the link in browser
    driver.get("https://alchemy.hguy.co/jobs/wp-admin")

    # Login
    driver.find_element(By.ID, "user_login").send_keys("root")
    driver.find_element(By.ID, "user_pass").send_keys("pa$$w0rd")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # Validate user is logged in
    loginMsg = driver.find_element(By.CLASS_NAME, "display-name").text
    assert loginMsg == "root"

    # Close the browser
    driver.quit()