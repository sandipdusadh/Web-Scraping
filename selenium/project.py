import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
query = "laptop"
file = 0
os.makedirs("data", exist_ok=True)
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=234WC15ZUST3N&sprefix=lap%2Caps%2C432&ref=nb_sb_noss_2")

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} item found")
    for elem in elems:
       d = elem.get_attribute("outerHTML")
       with open(f"data/{query}_{file}.html", "w",encoding = "utf-8") as f:
           f.write(d)
           file +=1
    # print(elems.text)
    # print(elems.get_attribute("outerHTML"))

    time.sleep(6)

driver.quit()