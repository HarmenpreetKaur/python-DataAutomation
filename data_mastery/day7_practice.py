import pandas as pd

# Sample dataset with text-based dates
data = {
    'Client': ['TechCorp', 'TechCorp', 'DesignHub', 'DesignHub', 'TechCorp'],
    'Service': ['Web Dev', 'SEO', 'Web Dev', 'Design', 'SEO'],
    'Date_Submitted': ['2023-01-15', '02/10/2023', '2023-01-20', '03/05/2023', '2023-03-12'],
    'Amount': [1500, 800, 1200, 950, 850]
}

df = pd.DataFrame(data)
print("=== ORIGINAL DATAFRAME ===")
print(df)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 1. Converting Text to DateTime
# -------------------------------------------------------------
# Pandas is smart enough to figure out most date formats automatically
df['Date_Submitted'] = pd.to_datetime(df['Date_Submitted'], format='mixed', errors='coerce')

print("=== AFTER DATETIME CONVERSION ===")
print(df)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 2. Extracting Month and Year
# -------------------------------------------------------------
df['Month'] = df['Date_Submitted'].dt.month
df['Year'] = df['Date_Submitted'].dt.year

print("=== WITH EXTRACTED MONTH AND YEAR ===")
print(df)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 3. Creating a Pivot Table
# -------------------------------------------------------------
pivot_report = pd.pivot_table(
    df, 
    values='Amount',       # The numbers to do math on
    index='Client',        # The rows
    columns='Service',     # The columns
    aggfunc='sum',         # The math operation
    fill_value=0           # Replace NaNs (when a client didn't buy a service) with 0
)

print("=== PIVOT TABLE REPORT ===")
print(pivot_report)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 4. Exporting to CSV
# -------------------------------------------------------------
# index=True is used here because our Pivot Table uses the Client names as the index!
pivot_report.to_csv('client_summary_report.csv', index=True)

print("Success! Check your VS Code file explorer for 'client_summary_report.csv'")