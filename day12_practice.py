import pandas as pd
import glob
import os

# -------------------------------------------------------------
# 1. Create Dummy Files (The Client's Mess)
# -------------------------------------------------------------
pd.DataFrame({'Month': ['January'], 'Revenue': [1500]}).to_csv('client_jan.csv', index=False)
pd.DataFrame({'Month': ['February'], 'Revenue': [2200]}).to_csv('client_feb.csv', index=False)
pd.DataFrame({'Month': ['March'], 'Revenue': [3100]}).to_csv('client_mar.csv', index=False)

print("Created 3 separate monthly CSV files in your folder!")
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 2. Scan the Folder
# -------------------------------------------------------------
# The '*' acts as a wildcard. It tells Python:
# "Find ANY file that starts with 'client_' and ends with '.csv'"
file_list = glob.glob('client_*.csv')

print(f"Python found {len(file_list)} files matching the pattern:")
print(file_list)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 3. Read and Combine (The Automation)
# -------------------------------------------------------------
# Create an empty list to hold our temporary DataFrames
dataframes = []

for file in file_list:
    # Read the current CSV file
    df = pd.read_csv(file)
    
    # Add it to our storage list
    dataframes.append(df)
# Now, stack all those DataFrames on top of each other!
# ignore_index=True resets the row numbers so they flow smoothly 0, 1, 2...
master_df = pd.concat(dataframes, ignore_index=True)

print("=== COMBINED MASTER DATAFRAME ===")
print(master_df)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 4. Export the Master File
# -------------------------------------------------------------
master_df.to_csv('master_client_report.csv', index=False)
print("Automation complete. Saved everything to 'master_client_report.csv'!")