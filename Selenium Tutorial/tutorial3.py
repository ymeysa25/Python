# Selenium Tutorial 3
# Pages Navigating and clicking Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = r"C:\Program Files (x86)\chromedriver.exe"
URL = "https://techwithtim.net/"

driver = webdriver.Chrome(PATH)
driver.get(URL)

# Access element that has text "Python Programming"
link = driver.find_element_by_link_text("Python Programming")

# Click "Python Programming" link, so we can move to the next page
link.click()

# Browser need time before accessing to the pages, to make sure there is no error, we can use WebDriverWait.
# so we can wait till page finished loading
try:
    second = 10  # Max Time

    # Get "Beginner Python Tutorials" link element
    element = WebDriverWait(driver, second).until(
        EC.presence_of_element_located(By.LINK_TEXT, "Beginner Python Tutorials")
    )
    element.click()

    # Get Getting Started Button element
    element = WebDriverWait(driver, second).until(
        EC.presence_of_element_located(By.ID, "sow-button-19310003")
    )

    element.click()

    # Back to previous in one page
    driver.back()
    driver.back()

    # Back to forward in one page
    driver.forward()

except:
    driver.quit()

# we can navigate to the browser using click() as long as the element is click able
