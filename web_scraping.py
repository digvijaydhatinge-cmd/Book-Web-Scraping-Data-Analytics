
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import time

# Project: CodeAlpha Web Scraping
# Website: Books to Scrape

BASE_URL = "https://books.toscrape.com/"

# Store all book records
book_data = []

# Step 1: Visit all 50 pages
for page in range(1, 51):

    # Step 2: Generate page URL
    if page == 1:
        url = BASE_URL
    else:
        url = f"{BASE_URL}catalogue/page-{page}.html"

    print(f"Scraping page {page}/50...")

    try:
        # Step 3: Download website HTML
        response = requests.get(url, timeout=20)
        response.raise_for_status()

        # Step 4: Save first page HTML
        if page == 1:
            with open("books_page.html", "w", encoding="utf-8") as file:
                file.write(response.text)

        # Step 5: Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Step 6: Find all books
        books = soup.find_all("article", class_="product_pod")

        # Step 7: Extract book information
        for book in books:

            title = book.h3.a["title"]

            price = book.find(
                "p", class_="price_color"
            ).text.strip()

            rating = book.find(
                "p", class_="star-rating"
            )["class"][1]

            availability = book.find(
                "p", class_="instock availability"
            ).text.strip()

            book_data.append({
                "Book Name": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability
            })

        # Wait before next request
        time.sleep(1)

    except requests.RequestException as error:
        print(f"Error on page {page}: {error}")
        continue

# Step 8: Convert records into DataFrame
df = pd.DataFrame(book_data)

# Step 9: Save all records into CSV
df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")

# Step 10: Display final results
print("\n========== SCRAPING REPORT ==========")
print("Total books collected:", len(df))
print("Total pages attempted: 50")
print("HTML file: books_page.html")
print("CSV file: books_data.csv")
print("=====================================")

print("\nFirst 5 records:")
print(df.head().to_string(index=False))

print("\nScraping completed!")

# STEP 4: DATA CLEANING

# Read CSV file
df = pd.read_csv("books_data.csv")

print("\nOriginal data:")
print(df.head())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Remove duplicate books
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Remove currency symbol and convert price to number

df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace(r"[^\d.]", "", regex=True)
    .astype(float)
)

# Save cleaned data
df.to_csv("cleaned_books_data.csv", index=False)

print("\nCleaned data:")
print(df.head())

print("\nTotal cleaned books:", len(df))
print("Data cleaning completed!")

# STEP 5: DATA ANALYSIS

# Read cleaned data
df = pd.read_csv("cleaned_books_data.csv")

# 1. Total number of books
print("\nTotal Books:", len(df))

# 2. Average price
print("Average Price:", df["Price"].mean())

# 3. Highest price
print("Highest Price:", df["Price"].max())

# 4. Lowest price
print("Lowest Price:", df["Price"].min())

# 5. Most expensive book
print("\nMost Expensive Book:")
print(df.loc[df["Price"].idxmax()])

# 6. Cheapest book
print("\nCheapest Book:")
print(df.loc[df["Price"].idxmin()])

# 7. Count books by rating
print("\nBooks by Rating:")
print(df["Rating"].value_counts())

# Bar Chart: Books by Rating

rating_counts = df["Rating"].value_counts()

rating_order = ["One", "Two", "Three", "Four", "Five"]

rating_counts = rating_counts.reindex(rating_order)

plt.figure(figsize=(8, 5))

plt.bar(rating_counts.index, rating_counts.values)

plt.title("Number of Books by Rating")
plt.xlabel("Book Rating")
plt.ylabel("Number of Books")

plt.show()
# Histogram: Book Price Distribution

plt.figure(figsize=(8, 5))

plt.hist(df["Price"], bins=10, edgecolor="black")

plt.title("Distribution of Book Prices")
plt.xlabel("Book Price (£)")
plt.ylabel("Number of Books")

plt.show()
# Pie Chart: Books by Rating

plt.figure(figsize=(7, 7))

plt.pie(
    rating_counts.values,
    labels=rating_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Books by Rating Percentage")

plt.show()