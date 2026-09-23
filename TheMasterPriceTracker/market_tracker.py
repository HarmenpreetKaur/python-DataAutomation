from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import sqlite3
import pandas as pd
import plotly.express as px


print("PHASE 1: EXTRACTION")
print("1. Launching the browser...")

# Open Chrome and navigate to the target URL
driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")

# Tell Selenium to wait up to 5 seconds if it can't find an element immediately
driver.implicitly_wait(5)

print("2. Scanning the page for products...")
# Find all 20 book containers on the main page
book_containers = driver.find_elements(By.CLASS_NAME, "product_pod")

scraped_data = []
print("3. Extracting and cleaning data...")

# Generate today's date for our database records
today_date = datetime.now().strftime("%Y-%m-%d")

print("3. Extracting data...")
for book in book_containers:
    h3_tag = book.find_element(By.TAG_NAME, "h3")
    a_tag = h3_tag.find_element(By.TAG_NAME, "a")
    title = a_tag.get_attribute("title")
    
    price_text = book.find_element(By.CLASS_NAME, "price_color").text
    clean_price = float(price_text.replace('£', ''))
    
    scraped_data.append((today_date, title, clean_price))

driver.quit()
print(f"SUCCESS: Extracted {len(scraped_data)} books.")


print("\nPHASE 2: LOAD")
print("4. Securing data in SQLite Database...")

# Connect to (or create) the database file
conn = sqlite3.connect("market_prices.db")
cursor = conn.cursor()

# Define the architecture of our table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book_prices (
        date_scraped TEXT,
        book_title TEXT,
        price REAL
    )
''')

# For testing purposes, clear out old data so we don't infinitely stack duplicates
cursor.execute('DELETE FROM book_prices')

# Inject the list of tuples we generated in Phase 1
cursor.executemany("INSERT INTO book_prices VALUES (?, ?, ?)", scraped_data)
conn.commit()

print("SUCCESS: Data locked in the database.")

print("\nPHASE 3: VISUALIZE")
print("5. Generating executive dashboard...")

# Query the database to get only the top 10 most expensive books
query = "SELECT * FROM book_prices ORDER BY price DESC LIMIT 10"
df = pd.read_sql_query(query, conn)
conn.close()

# Build a horizontal bar chart
fig = px.bar(
    df, 
    x='price', 
    y='book_title', 
    orientation='h',
    title="Premium Market Analysis: Top 10 Highest Priced Assets",
    labels={'price': 'Listed Price (£)', 'book_title': ''}
)

# Apply your designer's eye to the layout
fig.update_layout(
    template='plotly_dark',
    yaxis={'categoryorder': 'total ascending'},  # Forces the most expensive item to the top
    title_font=dict(size=22, family="Helvetica"),
    margin=dict(l=20, r=40, t=80, b=40),         # Clean negative space
    hovermode='y unified'
)

# Export to HTML
output_file = "market_report.html"
fig.write_html(output_file)

print(f"SUCCESS: Pipeline complete! Open '{output_file}' in your web browser.")