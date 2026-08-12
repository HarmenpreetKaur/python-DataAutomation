import pandas as pd

# -------------------------------------------------------------
# 1. Creating a Series (1D array - single column of data)
# -------------------------------------------------------------
scores = pd.Series([88, 92, 79, 95], name="Score")
print("--- 1D Series Output ---")
print(scores)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 2. Creating a DataFrame manually from a Python Dictionary
# -------------------------------------------------------------
data = {
    'Player': ['Alex', 'Jordan', 'Taylor', 'Morgan'],
    'Team': ['Red', 'Blue', 'Red', 'Blue'],
    'Points': [18, 24, 15, 30],
    'Rebounds': [5, 8, 3, 11]
}

df_manual = pd.DataFrame(data)
print("--- Manually Created DataFrame ---")
print(df_manual)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 3. Reading Data from an external CSV file
# -------------------------------------------------------------
df_csv = pd.read_csv('players.csv')
print("--- Data Read from players.csv ---")
print(df_csv)
print("\n" + "="*40 + "\n")


# Load the dataset created in Step 2
df = pd.read_csv('players.csv')

print("=== 1. PREVIEW DATA (.head) ===")
# Previews the first 3 rows (defaults to 5 if empty)
print(df.head(3))
print("\n")

print("=== 2. CHECK DIMENSIONS (.shape) ===")
# Returns a tuple: (number of rows, number of columns)
print("Shape (Rows, Columns):", df.shape)
print("\n")

print("=== 3. CHECK COLUMN TYPES & NULLS (.info) ===")
# Prints column names, non-null counts, and data types (int64, object/string, float, etc.)
df.info()
print("\n")

print("=== 4. GENERATE STATISTICAL SUMMARY (.describe) ===")
# Calculates count, mean, std, min, percentiles (25%, 50%, 75%), and max for numeric columns
print(df.describe())

print(df.head(2))