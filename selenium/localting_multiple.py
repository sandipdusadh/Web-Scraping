import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the Chrome driver outside the loop
driver = webdriver.Chrome()
query = "laptop"

# Loop through pages 1 to 19
for i in range(1, 20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=234WC15ZUST3N&sprefix=lap%2Caps%2C432&ref=nb_sb_noss_2")
    
    # Wait for the products to load on the page
    time.sleep(4)

    # Use find_elements (plural) to get a list of all matching elements
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    
    print(f"--- Page {i}: {len(elems)} items found ---")
    
    # Iterate through the list of elements
    for elem in elems:
        if elem.text.strip():  # Only print if there is text content
            print(elem.text)
            print("-" * 20)

# Close the browser only AFTER the loop finishes
driver.close()
