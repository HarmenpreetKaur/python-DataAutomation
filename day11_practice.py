import requests
import pandas as pd
from datetime import datetime

# -------------------------------------------------------------
# 1. Connect to the API
# -------------------------------------------------------------
# This is a public API endpoint that requires no passwords
url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)
print(f"API Connection Status: {response.status_code}")

# -------------------------------------------------------------
# 2. Parse the JSON Data
# -------------------------------------------------------------
# .json() instantly converts the raw response into a Python dictionary
data = response.json()

print("\n=== RAW JSON DATA ===")
print(data)

# -------------------------------------------------------------
# 3. Extract Specific Data Points
# -------------------------------------------------------------
# Dig into the dictionary to grab exactly what we want
latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']
raw_timestamp = data['timestamp']

# The API gives us time in "Unix Epoch" (seconds since 1970)
# Let's convert it to a readable date and time
readable_time = datetime.fromtimestamp(raw_timestamp)

print(f"\nAt exactly {readable_time}, the ISS was located at:")
print(f"Latitude: {latitude}, Longitude: {longitude}")

# -------------------------------------------------------------
# 4. Package for the Client
# -------------------------------------------------------------
iss_data = [{
    'Timestamp': readable_time,
    'Latitude': latitude,
    'Longitude': longitude
}]

df = pd.DataFrame(iss_data)

print("\n=== FINAL DATAFRAME ===")
print(df)

# You can export this to CSV just like always!
df.to_csv('iss_location.csv', index=False)