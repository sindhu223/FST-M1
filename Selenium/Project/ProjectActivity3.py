# Import webdriver from selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Set up the Firefox Driver with WebDriverManger
service = FirefoxService(GeckoDriverManager().install())

# Set up the Firefox Driver with WebDriverManger
with webdriver.Firefox(service=service) as driver:
    # Navigate to the URL

    driver.get("https://alchemy.hguy.co/jobs/")
    headerImage = driver.find_element(By.XPATH,"//img[@class='attachment-large size-large wp-post-image']")
    imageUrl = headerImage.get_attribute("src")
    print("header image url: " + imageUrl)
