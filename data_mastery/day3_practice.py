import pandas as pd
import numpy as np

# Simulated Messy Client Data
data = {
    'Client_Name': ['  TechCorp ', 'StartupInc', 'TechCorp ', 'DataWorks', np.nan, '  AI_Solutions '],
    'Project': ['Web Scraping', 'API Integration', 'Web Scraping', 'Data Cleaning', 'Dashboard', 'Machine Learning'],
    'Invoice_Amount': [150, np.nan, 150, 300, 450, 600],
    'Status': ['Paid', 'Pending', 'Paid', np.nan, 'Pending', 'Paid']
}

df = pd.DataFrame(data)
print("=== RAW, MESSY DATAFRAME ===")
print(df)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 1. Identifying Missing Data
# -------------------------------------------------------------
# .isna() returns True for missing values. .sum() counts them per column.
missing_counts = df.isna().sum()
print("=== Missing Values Per Column ===")
print(missing_counts)
print("\n")

# -------------------------------------------------------------
# 2. Dropping Missing Data (.dropna)
# -------------------------------------------------------------
# Drop any row that contains at least one NaN
df_dropped_rows = df.dropna()
print("=== DataFrame after dropna() ===")
# PRO-TIP: Drop rows ONLY if a specific column is missing
df_dropped_specific = df.dropna(subset=['Invoice_Amount'])
print(df_dropped_rows)
print("\n")
print("=== DataFrame after dropna(subset=['Invoice_Amount']) ===")
print(df_dropped_specific)
print("\n")

# -------------------------------------------------------------
# 3. Filling Missing Data (.fillna)
# -------------------------------------------------------------
# Instead of dropping, let's fill missing invoices with 0 and statuses with 'Unknown'
df_filled = df.copy() # Make a copy so we don't alter the original yet
df_filled['Invoice_Amount'] = df_filled['Invoice_Amount'].fillna(0)
df_filled['Status'] = df_filled['Status'].fillna('Unknown')
# ADVANCED PRO-TIP: Fill a missing number with the column's average
average_invoice = df['Invoice_Amount'].mean()
df['Invoice_Amount'] = df['Invoice_Amount'].fillna(average_invoice)

print("=== DataFrame after fillna() ===")
print(df_filled)
print("\n")
print("=== DataFrame after fillna() with average Invoice_Amount ===")
print(df)
print("\n" + "="*40 + "\n")
# -------------------------------------------------------------
# Dropping Duplicate Rows
# -------------------------------------------------------------
# Let's use our df_filled dataframe from the previous step
print("=== Checking for Duplicates ===")
print(df_filled.duplicated()) # Returns True for row 2 (the duplicate TechCorp)
print("\n")

# Remove the duplicates (keep the first occurrence by default)
df_unique = df_filled.drop_duplicates()

print("=== DataFrame after drop_duplicates() ===")
print(df_unique)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# Cleaning Text Data
# -------------------------------------------------------------
# 1. Strip extra whitespace from the beginning and end of strings
df_unique['Client_Name'] = df_unique['Client_Name'].str.strip()

# 2. Convert a column to fully uppercase (or lowercase with .str.lower())
df_unique['Status'] = df_unique['Status'].str.upper()

# 3. Replace specific characters (e.g., replacing underscores with spaces)
df_unique['Client_Name'] = df_unique['Client_Name'].str.replace('_', ' ')

print("=== FINAL CLEANED DATAFRAME ===")
print(df_unique)

filterdf=df_unique[df_unique['Status']=='PAID']
print("\n=== Filtered DataFrame (Status == 'PAID') ===")
print(filterdf)
print(filterdf['Invoice_Amount'].sum())