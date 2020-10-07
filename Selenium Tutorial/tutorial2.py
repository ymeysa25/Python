# Selenium Tutorial 2
"""
    - Locating Element from html

    Note:
        There are several method to access element by:
        - id, name, class, tag, XPATH

        to get XPATH, find part element that want to locate, right click find copy XPATH
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = r"C:\Program Files (x86)\chromedriver.exe"
URL = "https://techwithtim.net/"

driver = webdriver.Chrome(PATH)
driver.get(URL)

# print all page source code
# print(driver.page_source)

# Get Search box element
search_box = driver.find_element_by_name("s")

# input "test" in search box
search_box.send_keys("test")

# Keys.RETURN same like ENTER in keyboard
search_box.send_keys(Keys.RETURN)

"""
    After sending "test" in searching box, browser need time to loading the pages before we can scraping data from it,
    to handle this problem, we could simply using WebDriverWait, so we can wait till page finished loading 
"""

try:
    # Max time
    second = 10

    # Get element by Id "main"
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    # Get all article tag name, note -> "elements" mean plural
    articles = main.find_elements_by_tag_name("article")

    # Print all summary in article tag
    for article in articles:
        summary = article.find_element_by_class_name("entry-summary")
        print("====================================")
        print(summary.text)

except:
    driver.quit()

