# Selenium tutorial 1
"""
    1. Installing library
    2. Downloading Web Driver
    3. Open Browser with Selenium
"""
# pip install selenium
# https://sites.google.com/a/chromium.org/chromedriver/downloads

# Import selenium library
from selenium import webdriver

# Driver PATH
PATH = r"C:\Program Files (x86)\chromedriver.exe"

# the URL we want to open
URL = "https://techwithtim.net/"

# Instance of Chrome WebDriver is created.
driver = webdriver.Chrome(PATH)

# Open Browser with the URL
driver.get(URL)

# Get website title
print(driver.title)

# Close current Tab Browser
driver.close()

# Close the Browser
driver.quit()
