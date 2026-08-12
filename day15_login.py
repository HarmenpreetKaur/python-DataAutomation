from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("1. Opening the browser...")
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

print("2. Waiting for the login form to appear...")
# Tell Python to wait up to 10 seconds, but proceed immediately once it finds the 'username' box
wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))

print("3. Injecting credentials...")
# The username field is already saved in our variable from Step 2
username_field.send_keys("tomsmith")

# Find the password field and type the password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

print("4. Clicking submit...")
login_button = driver.find_element(By.CLASS_NAME, "radius")
login_button.click()

# Verify the login was successful by checking the new URL
if "secure" in driver.current_url:
    print("SUCCESS: We have breached the mainframe (logged in)!")
else:
    print("FAILED: Did not reach the secure area.")

# Keep the browser open for 5 seconds so you can see the result, then close it
import time
time.sleep(5)
driver.quit()