import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Mute any Seaborn version warnings to keep the terminal professional
warnings.filterwarnings("ignore")

print("Initiating Data Pipeline...")

# ==============================================================
# PHASE 1: EXTRACTION (The API Call)
# ==============================================================
print("1. Fetching live data from API...")

# We are using Open-Meteo, a free API that requires no passwords.
# This specific URL requests the last 7 days of hourly temperatures.
url = "https://api.open-meteo.com/v1/forecast?latitude=41.28&longitude=13.24&past_days=7&hourly=temperature_2m"

response = requests.get(url)

if response.status_code == 200:
    print("   -> Success! Connected to server.")
    raw_data = response.json()
else:
    print(f"   -> Error: Server returned status {response.status_code}")
    exit() # Stop the script if the connection fails


# ==============================================================
# PHASE 2: TRANSFORMATION (Pandas Cleaning)
# ==============================================================
print("2. Cleaning and structuring data...")

# Dig into the nested JSON to pull out the lists of times and temperatures
times = raw_data['hourly']['time']
temperatures = raw_data['hourly']['temperature_2m']

# Build a Pandas DataFrame out of the raw lists
df = pd.DataFrame({
    'Timestamp': times,
    'Temperature_C': temperatures
})

# The API sends dates as messy strings like "2023-10-25T08:00".
# Let's use our Day 7 skills to convert them into real DateTime objects.
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Extract just the date for daily grouping
df['Date'] = df['Timestamp'].dt.date

# Calculate the Average Daily Temperature using GroupBy
daily_summary = df.groupby('Date')['Temperature_C'].mean().reset_index()


# ==============================================================
# PHASE 3: VISUALIZATION (Seaborn & Matplotlib)
# ==============================================================
print("3. Generating visual report...")

plt.figure(figsize=(10, 6))
sns.set_theme(style="darkgrid")

# Create a sleek line chart
sns.lineplot(
    data=daily_summary, 
    x='Date', 
    y='Temperature_C', 
    color='#e74c3c', 
    linewidth=3,
    marker='o',
    markersize=8
)

plt.title("Average Daily Temperature (Past 7 Days)", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.xticks(rotation=45) # Tilt the dates so they don't overlap
plt.tight_layout()

# Save the chart as an image file directly to the hard drive!
plt.savefig("temperature_trend_report.png")
print("   -> Chart saved as 'temperature_trend_report.png'")


# ==============================================================
# PHASE 4: EXPORTING (File Management)
# ==============================================================
print("4. Exporting data to CSV...")

daily_summary.to_csv("daily_temperature_summary.csv", index=False)
print("   -> Data saved to 'daily_temperature_summary.csv'")

print("\n=== PIPELINE COMPLETE ===")