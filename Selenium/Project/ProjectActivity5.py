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

    # Find the navigation bar element
    navigationBar = driver.find_element(By.ID("menu-item-24"))

    # Find the "Jobs" menu item and click it
    jobsMenuItem = navigationBar.find_element(By.LINK_TEXT("Jobs"))
    jobsMenuItem.click()

    # Read the page title
    pageTitle = driver.Title()

    # Verify the correct page using the page title
    expectedTitle = "Jobs – Alchemy Jobs"
    assert  == expectedTitle,f"page title is '{pageTitle}',but expected '{expectedTitle}'"

    # Print success message if the verification is successful
    print("You are on the correct page.")
