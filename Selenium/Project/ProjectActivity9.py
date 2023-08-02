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
    driver.implicitly_wait(20)

    # Navigate to Job Listings and add new job
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/ul/li[7]/a/div[3]").click()
    driver.find_element(By.CLASS_NAME, "page-title-action").click()
    driver.find_element(By.CSS_SELECTOR, ".components-modal__header > button:nth-child(2)").click()
    driver.implicitly_wait(20)
    driver.find_element(By.ID, "post-title-0").send_keys("Managing Consultant")
    driver.implicitly_wait(20)
    driver.find_element(By.CSS_SELECTOR, "button.components-button:nth-child(3)").click()
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div[1]/div/div/div[1]/div/div[2]/div[3]/div/div/div/div[1]/div/button").click()

    # Validate job is created
    publishedMessage = driver.find_element(By.CSS_SELECTOR, ".post-publish-panel__postpublish-header").text
    assert publishedMessage == "Managing Consultant is now live."

    # Assert new job reflects in Jobs page
    driver.get("https://alchemy.hguy.co/jobs/jobs/")
    driver.find_element(By.ID, "search_keywords").send_keys("Managing Consultant")
    driver.find_element(By.XPATH, "//input[@value='Search Jobs']").click()
    driver.implicitly_wait(20)
    jobName = driver.find_element(By.CLASS_NAME, "position").text
    assert jobName == "Managing Consultant"
    print("Managing Consultant Job is posted successfully")

    # Close the browser
    driver.quit()