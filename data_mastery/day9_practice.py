import requests
from bs4 import BeautifulSoup
import pandas as pd

# -------------------------------------------------------------
# 1. Visit the Website
# -------------------------------------------------------------
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

# A status code of 200 means the server let us in successfully
print(f"Server Status Code: {response.status_code}") 
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 2. Parse the HTML code
# -------------------------------------------------------------
soup = BeautifulSoup(response.text, 'html.parser')

# Let's test it by grabbing the main title of the webpage
page_title = soup.title.text
print(f"The title of the webpage is: '{page_title}'")
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 3. Find and Extract
# -------------------------------------------------------------
# Find all HTML <div> tags that have the class 'quote'
quote_blocks = soup.find_all('div', class_='quote')

# Create an empty list to hold our final data
extracted_data = []

for block in quote_blocks:
    # Rip the text out of the specific HTML tags
    text = block.find('span', class_='text').text
    author = block.find('small', class_='author').text
    
    # Save it as a dictionary
    extracted_data.append({
        'Author': author, 
        'Quote': text
    })

print(f"Successfully extracted {len(extracted_data)} quotes!")
print("\n" + "="*40 + "\n") 

# -------------------------------------------------------------
# 4. Convert to Pandas and Export
# -------------------------------------------------------------
df = pd.DataFrame(extracted_data)

print("=== FINAL SCRAPED DATAFRAME ===")
print(df.head())

# Export it for the client
df.to_csv('scraped_quotes.csv', index=False)
print("\nData successfully saved to 'scraped_quotes.csv'")