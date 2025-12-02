import requests, random, time, csv
from bs4 import BeautifulSoup
from pathlib import Path

OUT = Path("data_raw/scraped")
OUT.mkdir(parents=True, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0"}
url = "https://books.toscrape.com/"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

books = []
for book in soup.select(".product_pod"):
    title = book.h3.a["title"]
    price = book.select_one(".price_color").get_text()
    books.append({"title": title, "price": price})

with open(OUT / "books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price"])
    writer.writeheader()
    writer.writerows(books)
import csv

# Save data
csv_path = OUT / "books.csv"

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "price"])  # header
    writer.writerows(books)

print(f"Saved scraped data to: {csv_path}")
