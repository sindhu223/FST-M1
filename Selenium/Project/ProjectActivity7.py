from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Set up the Firefox Driver with WebDriverManger
service = FirefoxService(GeckoDriverManager().install())

# Start the Driver
with webdriver.Firefox(service=service) as driver:

    # Open the link in browser
    driver.get("https://alchemy.hguy.co/jobs")

    # Initialize wait object
    wait = WebDriverWait(driver, 30);

    # Enter the details for new job creation
    driver.find_element(By.ID, "menu-item-26").click()
    driver.find_element(By.ID, "create_account_email").send_keys("testjob78@gmail.com")
    driver.find_element(By.ID, "job_title").send_keys("Junior Consultant")
    driver.find_element(By.ID, "job_location").send_keys("Bangalore")
    driver.find_element(By.ID, "job_description_ifr").send_keys("Test Job creation")
    driver.find_element(By.ID, "application").send_keys("https://lms.training-support.net")
    driver.find_element(By.ID, "company_name").send_keys("ABC Marketing Ltd")
    driver.find_element(By.ID, "company_website").send_keys("https://alchemy.hguy.co")
    driver.find_element(By.ID, "company_tagline").send_keys("Test")
    driver.find_element(By.ID, "company_video").send_keys("https://www.youtube.com/watch?v=QM2-MX1Lz-A")
    driver.find_element(By.ID, "company_twitter").send_keys("@Twitter")
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, "//input[@value='Preview']").click()
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, "//input[@value='Submit Listing']").click()
    driver.implicitly_wait(20)

    # Validate if Job created successfully
    driver.find_element(By.ID, "menu-item-24").click()
    driver.find_element(By.ID, "search_keywords").send_keys("ABC Marketing Ltd")
    driver.find_element(By.XPATH, "//input[@value='Search Jobs']").click()
    driver.implicitly_wait(20)
    jobName = driver.find_element(By.CLASS_NAME, "position").text
    assert jobName == "Junior Consultant\nABC Marketing Ltd Test"

    # Close the browser
    driver.quit()