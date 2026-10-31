# Book Web Scraping and Data Analytics Project

## 1. Project Overview

This project focuses on collecting book information from the website Books to Scrape using Python. The collected data is cleaned, analyzed, and visualized to understand book prices, ratings, and availability.

A total of 1,000 books were collected from 50 pages.

## 2. Objectives

- Collect book details from a website.
- Extract book names, prices, ratings, and availability.
- Clean and organize the collected data.
- Perform data analysis using Pandas.
- Create graphs to understand the results.

## 3. Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib
- Visual Studio Code

## 4. Project Methodology

### Step 1: Web Scraping
Used Python Requests and BeautifulSoup to extract book information from Books to Scrape.

### Step 2: Data Collection
Collected the following information:
- Book Name
- Price
- Rating
- Availability

### Step 3: Data Cleaning
Used Pandas to clean the collected data, remove duplicate records, check missing values, and convert book prices into numeric values.

### Step 4: Data Analysis
Analyzed book prices and ratings to find useful information.

### Step 5: Data Visualization
Created three graphs using Matplotlib:
- Bar Chart: Number of books by rating.
- Histogram: Distribution of book prices.
- Pie Chart: Percentage of books by rating.

## 5. Project Results

- Total Books Collected: 1,000
- Total Pages Scraped: 50
- Average Book Price: £35.07
- Highest Book Price: £59.99
- Lowest Book Price: £10.00

## 6. Project Files

- `books_data.csv` – Original scraped data.
- `cleaned_books_data.csv` – Cleaned dataset.
- `books_page.html` – Saved webpage HTML.
- `graphs/` – Contains three visualization images.
- `README.md` – Project documentation.

## 7. Conclusion

This project demonstrates how Python can be used for web scraping, data cleaning, data analysis, and data visualization. It helped in understanding how to collect raw data from websites and convert it into meaningful information.