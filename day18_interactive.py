import pandas as pd
import plotly.express as px

print("1. Generating client data...")

# Mock dataset: Monthly sales for two different tech products
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'] * 2,
    'Sales_Euros': [1200, 1500, 1100, 1800, 2100, 2500, 
                    800, 950, 1300, 1200, 1600, 1900],
    'Product': ['AI Automation Bot'] * 6 + ['Web Scraping Tool'] * 6
}

df = pd.DataFrame(data)

print("2. Building the interactive canvas...")

# Create a line chart with markers
fig = px.line(
    df, 
    x='Month', 
    y='Sales_Euros', 
    color='Product',        # This automatically splits the lines and creates a legend
    markers=True,           # Adds dots at each data point for easier hovering
    title='Q1 & Q2 Revenue Tracking'
)

print("3. Applying styling and layout rules...")

fig.update_layout(
    template='plotly_white',                     # Uses a clean, white background
    hovermode='x unified',                       # A single hover line that shows data for both products at once
    title_font=dict(size=24, family="Arial"),    # Clean typography
    legend_title_text='Software Asset',
    margin=dict(l=40, r=40, t=60, b=40)          # Perfecting the negative space around the chart
)

# Soften the grid lines so they don't overpower the data
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#e5e5e5')

print("4. Exporting to HTML...")

# Save the interactive chart as a webpage
html_file = "interactive_revenue_report.html"
fig.write_html(html_file)

print(f"SUCCESS: Chart saved as '{html_file}'.")