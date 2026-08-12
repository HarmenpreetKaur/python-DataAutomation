import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')  # Suppress warnings for cleaner output

# Client Dataset: Your first 3 months of freelance revenue
data = {
    'Month': ['Month 1', 'Month 1', 'Month 2', 'Month 2', 'Month 3', 'Month 3'],
    'Service': ['Web Dev', 'Data Analysis', 'Web Dev', 'Data Analysis', 'Web Dev', 'Data Analysis'],
    'Revenue_EUR': [300, 150, 450, 400, 500, 650]
}

df = pd.DataFrame(data)
print("=== RAW DATA ===")
print(df)

# -------------------------------------------------------------
# 1. Total Revenue Trend (Line Chart)
# -------------------------------------------------------------
# Group the data to get total revenue per month
monthly_totals = df.groupby('Month')['Revenue_EUR'].sum().reset_index()

# Create a figure (the canvas) and define its size
plt.figure(figsize=(8, 5))

# Plot the line (x-axis, y-axis, color, and a marker for the data points)
plt.plot(monthly_totals['Month'], monthly_totals['Revenue_EUR'], color='#2c3e50', marker='o', linewidth=2)

# Add structure and context
plt.title('Total Freelance Revenue Growth', fontsize=14, pad=15)
plt.xlabel('Timeline')
plt.ylabel('Revenue (€)')
plt.grid(True, linestyle='--', alpha=0.6) # A subtle background grid

# This tells Python to actually render the window and show the art
plt.show()
# -------------------------------------------------------------
# 2. Revenue Breakdown by Service (Bar Chart)
# -------------------------------------------------------------
plt.figure(figsize=(9, 6))

# Set a cohesive aesthetic theme
sns.set_theme(style="whitegrid")

# Create a grouped bar chart
# hue='Service' automatically splits the bars and colors them differently
ax = sns.barplot(
    data=df, 
    x='Month', 
    y='Revenue_EUR', 
    hue='Service', 
    palette='mako' # A built-in, beautifully blended color palette
)

# Refine the typography and layout
plt.title('Revenue Breakdown: Web Dev vs. Data Analysis', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('') # Removing the x-label because "Month" is obvious
plt.ylabel('Revenue (€)', fontsize=12)

# Clean up the legend placement
plt.legend(title='Service Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout() # Ensures nothing gets cut off

plt.show()