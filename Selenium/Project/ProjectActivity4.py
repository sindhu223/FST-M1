# Import webdriver from selenium
import string

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
    secondHeading = driver.find_element(By.XPATH, "//h2[text()='Quia quis non']")
    imageHeader = secondHeading.text
    print("Second heading of webpage:", imageHeader)
