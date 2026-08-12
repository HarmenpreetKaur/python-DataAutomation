import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# -------------------------------------------------------------
# 1. Boot up the Robot Browser
# -------------------------------------------------------------
print("Starting the browser... look for a new Chrome window!")
driver = webdriver.Chrome()

# Tell the browser to navigate to our website
driver.get('http://quotes.toscrape.com/')

extracted_data = []

# -------------------------------------------------------------
# 2. Scrape Multiple Pages
# -------------------------------------------------------------
# We will tell it to scrape exactly 3 pages
for page in range(1, 4):
    print(f"Scraping Page {page}...")
    
    # Pause for 2 seconds. This gives the page time to load, 
    # and prevents the server from blocking us for going too fast.
    time.sleep(2)
    
    # Find all the quote containers (Selenium uses 'By.CLASS_NAME' instead of 'class_')
    quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote')
    
    # Extract the text and author from each block
    for block in quote_blocks:
        text = block.find_element(By.CLASS_NAME, 'text').text
        author = block.find_element(By.CLASS_NAME, 'author').text
        extracted_data.append({'Author': author, 'Quote': text})
        
    # -------------------------------------------------------------
    # 3. Find and Click the Next Button
    # -------------------------------------------------------------
    try:
        # Find the link that contains the word "Next"
        next_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Next')
        next_button.click() # Actually click it!
    except:
        # If the script can't find a Next button, we reached the final page
        print("No more pages found. Stopping.")
        break

# -------------------------------------------------------------
# 4. Clean Up and Export
# -------------------------------------------------------------
# Close the automated browser window
driver.quit()

# Convert to Pandas and save
df = pd.DataFrame(extracted_data)
print("\n=== SCRAPING COMPLETE ===")
print(f"Successfully scraped {len(df)} quotes across multiple pages!")

df.to_csv('selenium_multiple_pages.csv', index=False)
print("Saved to 'selenium_multiple_pages.csv'")