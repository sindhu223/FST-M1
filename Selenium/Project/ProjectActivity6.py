from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Set up the Firefox Driver with WebDriverManger
service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:

    # Open the link in browser
    driver.get("https://alchemy.hguy.co/jobs")

    # Initialize wait object
    wait = WebDriverWait(driver, 30);

    # Search and apply for job
    driver.find_element(By.ID, "menu-item-24").click()
    driver.find_element(By.ID, "search_keywords").send_keys("Banking")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    driver.implicitly_wait(20)
    driver.find_element(By.CLASS_NAME, "company_logo").click()
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, "//input[@value='Apply for job']").click()
    driver.implicitly_wait(20)

    # Get Job mail/website
    jobEmail = driver.find_element(By.CSS_SELECTOR, ".application_details > p:nth-child(1) > a:nth-child(1)").text
    print("Job web or email: " + jobEmail)

    # Close the browser
    driver.quit()

