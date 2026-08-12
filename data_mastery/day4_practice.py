import pandas as pd

# Sample dataset
data = {
    'Full Name': ['Alex Carter', 'Jordan Smith', 'Taylor Swift', 'Morgan Lee'],
    'hourly_rate_usd': [45, 60, 55, 40],
    'Hours Worked': [10, 15, 8, 20]
}

df = pd.DataFrame(data)
print("=== ORIGINAL DATAFRAME ===")
print(df)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 1. Renaming Columns (.rename)
# -------------------------------------------------------------
# Pass a dictionary: {'old_name': 'new_name'}
df_clean = df.rename(columns={
    'Full Name': 'full_name',
    'Hours Worked': 'hours_worked'
})

print("=== AFTER RENAMING COLUMNS ===")
print(df_clean)
print("\n")

# -------------------------------------------------------------
# 2. Dropping Columns (.drop)
# -------------------------------------------------------------
# If we didn't need the hours_worked column anymore:
# df_clean = df_clean.drop(columns=['hours_worked'])
# Pro-Tip: You might also see this written using 'axis'
# df_clean = df_clean.drop(['hours_worked'], axis=1) 
# (axis=1 tells Pandas to drop a column, axis=0 tells it to drop a row)

# -------------------------------------------------------------
# 3. Splitting Text Columns (.str.split)
# -------------------------------------------------------------
# The 'expand=True' argument splits the string into two separate columns!
df_clean[['first_name', 'last_name']] = df_clean['full_name'].str.split(' ', expand=True)

# Now drop the old combined column since we don't need it
df_clean = df_clean.drop(columns=['full_name'])

print("=== AFTER SPLITTING NAMES ===")
print(df_clean)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 4. Column Math
# -------------------------------------------------------------
# Calculate total payout (Rate * Hours)
df_clean['total_payout'] = df_clean['hourly_rate_usd'] * df_clean['hours_worked']

print("=== AFTER CALCULATED COLUMN ===")
print(df_clean)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 5. Using .apply() with Lambda
# -------------------------------------------------------------
# Add a 10% bonus if the payout is > 500, otherwise keep the original payout
df_clean['final_payout'] = df_clean['total_payout'].apply(lambda x: x * 1.10 if x > 500 else x)

print("=== FINAL DATAFRAME WITH APPLY() ===")
print(df_clean)

df_clean['rate_eur']=df_clean['hourly_rate_usd']*0.92  # Assuming 1 USD = 0.92 EUR
print(df_clean)