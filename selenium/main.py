import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to Python.org
driver.get("http://www.python.org")
assert "Python" in driver.title

# Locate the search bar
elem = driver.find_element(By.NAME, "q")
elem.clear()

# Type "pycon" and press Enter
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# Verify that results are displayed
assert "No results found." not in driver.page_source

# Wait and close the browser
time.sleep(6)
driver.close()