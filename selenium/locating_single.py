import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Target URL
query = "laptop"
url = f"https://www.amazon.in/s?k={query}&crid=234WC15ZUST3N&sprefix=lap%2Caps%2C432&ref=nb_sb_noss_2"
driver.get(url)

# Add a small delay to let the page fully load before searching for elements
time.sleep(3)

try:
    # Locate the first product card
    elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
    print("--- Text Content ---")
    print(elem.text)
    print("\n--- HTML Content ---")
    print(elem.get_attribute("outerHTML"))
except Exception as e:  # noqa: BLE001
    print(f"Error finding element: {e}")

# Wait and close the browser
time.sleep(6)
driver.close()
