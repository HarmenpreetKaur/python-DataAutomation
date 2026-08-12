import pandas as pd

# Client Dataset: Freelancer Project Invoices
data = {
    'Department': ['Web Dev', 'Data', 'Web Dev', 'SEO', 'Data', 'SEO'],
    'Freelancer': ['Alex', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Riley'],
    'Hours_Worked': [40, 35, 50, 20, 45, 15],
    'Billed_USD': [2000, 1750, 2500, 1000, 2250, 750]
}

df = pd.DataFrame(data)
print("=== ORIGINAL DATAFRAME ===")
print(df)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 1. Simple Grouping
# -------------------------------------------------------------
# Group by Department and calculate the total (sum) of all numerical columns
dept_totals = df.groupby('Department').sum(numeric_only=True)

print("=== TOTALS BY DEPARTMENT ===")
print(dept_totals)
print("\n")

# If you only care about ONE specific column (e.g., just Billed_USD):
dept_billing = df.groupby('Department')['Billed_USD'].sum()

print("=== TOTAL BILLED BY DEPARTMENT ===")
print(dept_billing)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 2. Multiple Aggregations with .agg()
# -------------------------------------------------------------
# We want the SUM of Hours_Worked, but the AVERAGE (mean) of Billed_USD
summary_stats = df.groupby('Department').agg({
    'Hours_Worked': 'sum',
    'Billed_USD': 'mean'
})

# Let's rename the columns so the client knows what they are looking at
summary_stats = summary_stats.rename(columns={
    'Hours_Worked': 'Total_Hours',
    'Billed_USD': 'Average_Billing'
})

print("=== DETAILED DEPARTMENT SUMMARY ===")
print(summary_stats)

# This is an advanced technique you will use constantly:
complex_summary = df.groupby('Department').agg({
    'Billed_USD': ['sum', 'mean', 'max']
})
complex_summary.columns = ['Total_Billed', 'Average_Billed', 'Max_Billed']

print("\n=== COMPLEX SUMMARY WITH MULTIPLE AGGREGATIONS ===")
print(complex_summary)