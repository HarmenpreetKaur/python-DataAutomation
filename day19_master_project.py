import requests
import sqlite3
import pandas as pd
import plotly.express as px
import warnings

# Mute warnings to keep the terminal output professional
warnings.filterwarnings("ignore")

print("Initiating Master Pipeline...")

# ==============================================================
# PHASE 1: EXTRACTION (Fetch Live Data)
# ==============================================================
print("1. Fetching live API data...")
# We are pulling 7 days of live temperature and humidity data for Terracina, Italy (Lat: 41.28, Lon: 13.24)
url = "https://api.open-meteo.com/v1/forecast?latitude=41.28&longitude=13.24&past_days=7&hourly=temperature_2m,relative_humidity_2m"
response = requests.get(url)
data = response.json()

# ==============================================================
# PHASE 2: LOAD (Secure Data in SQLite)
# ==============================================================
print("2. Securing data in SQLite Database...")
conn = sqlite3.connect("master_environmental_data.db")
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_logs (
        timestamp TEXT, 
        temperature REAL, 
        humidity REAL
    )
''')

# Clear old test data so we have a fresh dataset every time
cursor.execute('DELETE FROM weather_logs') 

# Extract the lists from the JSON and zip them together into rows
times = data['hourly']['time']
temps = data['hourly']['temperature_2m']
humidities = data['hourly']['relative_humidity_2m']
insert_records = list(zip(times, temps, humidities))

# Inject the rows into the database securely
cursor.executemany("INSERT INTO weather_logs VALUES (?, ?, ?)", insert_records)
conn.commit()

# ==============================================================
# PHASE 3: TRANSFORM (Pandas Data Cleaning)
# ==============================================================
print("3. Querying database and structuring data...")
# Pull the raw data right back out of the database into a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM weather_logs", conn)
conn.close()

# Clean dates and calculate daily averages
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['Date'] = df['timestamp'].dt.date
daily_df = df.groupby('Date').mean().reset_index()

# ==============================================================
# PHASE 4: VISUALIZE (Plotly Interactive Dashboard)
# ==============================================================
print("4. Generating interactive executive dashboard...")

# Build a dual-line chart for Temp and Humidity
fig = px.line(
    daily_df, 
    x='Date', 
    y=['temperature', 'humidity'], 
    title="7-Day Environmental Analytics (Terracina, Italy)",
    labels={'value': 'Metric Reading', 'variable': 'Sensor Data'}
)

# Apply a professional designer's touch to the layout
fig.update_layout(
    template='plotly_dark',                      # Sleek dark mode aesthetic
    hovermode='x unified',                       # Clean, unified hover tooltips
    title_font=dict(size=24, family="Helvetica"),
    margin=dict(l=40, r=40, t=80, b=40),
    legend_title_text='Metrics'
)

# Rename the legend labels for clarity
fig.for_each_trace(lambda t: t.update(name="Temp (°C)" if t.name == "temperature" else "Humidity (%)"))

# Export the final interactive file
output_file = "executive_dashboard.html"
fig.write_html(output_file)

print(f"\nSUCCESS: Pipeline complete! Open '{output_file}' in your web browser.")