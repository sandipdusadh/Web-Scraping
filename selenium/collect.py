import os
from urllib.parse import urljoin

import pandas as pd
from bs4 import BeautifulSoup

products = {"title": [], "price": [], "link": []}
for file in os.listdir("data"):
    if not file.endswith(".html"):
        continue

    with open(os.path.join("data", file), encoding="utf-8", errors="replace") as html_file:
        soup = BeautifulSoup(html_file.read(), "html.parser")

    title_tag = soup.find("h2")
    link_tag = title_tag.find_parent("a", href=True) if title_tag else None
    price_tag = soup.find("span", class_="a-price")

    if not title_tag or not link_tag or not price_tag:
        print(f"Skipping incomplete product: {file}")
        continue

    products["title"].append(title_tag.get_text(" ", strip=True))
    products["price"].append(price_tag.get_text(" ", strip=True))
    products["link"].append(urljoin("https://www.amazon.in", link_tag["href"]))

df = pd.DataFrame(products)
df.to_csv("data.csv", index=False)