import pandas as pd

# Client Dataset: Tech Freelancers & Rates
data = {
    'Name': ['Alex', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Riley'],
    'Role': ['Python Dev', 'Data Analyst', 'Python Dev', 'AI Specialist', 'Data Analyst', 'AI Specialist'],
    'Hourly_Rate': [45, 35, 55, 80, 40, 75],
    'Hours_Worked': [120, 160, 95, 110, 140, 85],
    'Remote': [True, False, True, True, False, True]
}

df = pd.DataFrame(data)
print("=== BASE DATAFRAME ===")
print(df)
print("\n" + "="*40 + "\n")

# =============================================================
# STEP 2: Column & Row Selection
# =============================================================

# 1. Selecting Columns (Series vs. DataFrame)
name_series = df['Name']
rates_df = df[['Name', 'Hourly_Rate']]

print("--- Single Column Output (Series) ---")
print(name_series)
print("\n--- Multiple Columns Output (DataFrame) ---")
print(rates_df)
print("\n" + "="*40 + "\n")

# 2. Position-Based Selection (.iloc)
# Format: df.iloc[row_positions, column_positions]
first_row = df.iloc[0]                  # First row, all columns
subset_iloc = df.iloc[0:3, 0:2]         # Rows 0-2, Columns 0-1

print("--- .iloc Slicing (Rows 0-2, Cols 0-1) ---")
print(subset_iloc)
print("\n" + "="*40 + "\n")

# 3. Label-Based Selection (.loc)
# Format: df.loc[row_labels, column_names]
subset_loc = df.loc[0:2, ['Name', 'Role', 'Hourly_Rate']]

print("--- .loc Slicing (Rows 0-2, Explicit Column Names) ---")
print(subset_loc)
print("\n" + "="*40 + "\n")

# =============================================================
# STEP 3: Conditional Selection & Filtering
# =============================================================

# 1. Single Condition Filtering
# Filter for freelancers earning more than $50/hour
high_earners = df[df['Hourly_Rate'] > 50]

print("--- High Earners (> $50/hr) ---")
print(high_earners[['Name', 'Role', 'Hourly_Rate']])
print("\n" + "="*40 + "\n")

# 2. Multiple Conditions (AND & OR)
# AND (&): Must be a 'Python Dev' AND work remotely
remote_python_devs = df[(df['Role'] == 'Python Dev') & (df['Remote'] == True)]

print("--- Remote Python Developers ---")
print(remote_python_devs[['Name', 'Role', 'Remote']])
print("\n")

# OR (|): Earns >= $75/hr OR worked more than 130 hours
high_value_workers = df[(df['Hourly_Rate'] >= 75) | (df['Hours_Worked'] > 130)]

print("--- High Rate (>=75) OR Long Hours (>130) ---")
print(high_value_workers[['Name', 'Hourly_Rate', 'Hours_Worked']])
print("\n" + "="*40 + "\n")

# 3. Filtering using .isin()
# Select freelancers who are either 'Python Dev' or 'AI Specialist'
target_roles = ['Python Dev', 'AI Specialist']
tech_specialists = df[df['Role'].isin(target_roles)]

print("--- Tech Specialists (Python Devs & AI Specialists) ---")
print(tech_specialists[['Name', 'Role']])
print("\n" + "="*40 + "\n")

# =============================================================
# STEP 4: Setting and Resetting Indexes
# =============================================================

# 1. Set 'Name' as the DataFrame index
df_indexed = df.set_index('Name')

print("--- DataFrame with 'Name' as Index ---")
print(df_indexed)
print("\n" + "="*40 + "\n")

# 2. Query a row directly by label using .loc
jordan_info = df_indexed.loc['Jordan']

print("--- Direct Lookup for 'Jordan' ---")
print(jordan_info)
print("\n" + "="*40 + "\n")

# 3. Reset the index back to default integer numbering (0, 1, 2...)
df_reset = df_indexed.reset_index()

print("--- DataFrame with Index Reset ---")
print(df_reset)
print("\n" + "="*40 + "\n")

remote_richs=df[(df["Remote"]==True)&(df["Hours_Worked"]>=100)]
print(remote_richs)
poorlancers=df[df["Hourly_Rate"]<50]
print(poorlancers[["Name","Hours_Worked"]])