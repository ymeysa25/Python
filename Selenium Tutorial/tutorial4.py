# Selenium Tutorial 2
# Action Chains and Automating Cookie Clicker
"""
    ActionChains are a way to automate low level interactions such as mouse movements, mouse button
actions, key press, and context menu interactions. This is useful for doing more complex actions
like hover over and drag and drop.
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = r"C:\Program Files (x86)\chromedriver.exe"
URL = "https://orteil.dashnet.org/cookieclicker/"

driver = webdriver.Chrome(PATH)
driver.get(URL)

# This method has same function with WebDriverWait, browser will wait for 5 seconds to make sure.
# The element we're looking for has finished loading
driver.implicitly_wait(5)

# Cookie Clicker element
cookie = driver.find_element_by_id("bigCookie")

# Amount cookie was clicked
cookie_count = driver.find_element_by_id("cookies")

items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

# Make ActionChains instance
actions = ActionChains(driver)

# click Cookie Clicker element
actions.click(cookie)

# We will click 1000 times
for i in range(1000):

    # Performs all stored actions.
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
