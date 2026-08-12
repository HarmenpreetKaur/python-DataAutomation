import pandas as pd

# Table 1: Freelancer Profiles
freelancers = pd.DataFrame({
    'Emp_ID': [101, 102, 103, 104],
    'Name': ['Alex', 'Jordan', 'Taylor', 'Morgan'],
    'Role': ['Web Dev', 'Data', 'SEO', 'Design']
})

# Table 2: Invoice Records
invoices = pd.DataFrame({
    'Invoice_No': ['INV-001', 'INV-002', 'INV-003'],
    'Emp_ID': [101, 102, 101], # Note: Alex (101) has two invoices. Taylor and Morgan have none.
    'Amount': [500, 750, 400]
})

print("=== TABLE 1: FREELANCERS ===")
print(freelancers)
print("\n=== TABLE 2: INVOICES ===")
print(invoices)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 1. Inner Merge (Intersection)
# -------------------------------------------------------------
# Merge on the 'Emp_ID' column. 
inner_merged = pd.merge(freelancers, invoices, on='Emp_ID', how='inner')

print("=== INNER MERGE (Matches Only) ===")
print(inner_merged)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 2. Left Merge (Keep all from Table 1)
# -------------------------------------------------------------
left_merged = pd.merge(freelancers, invoices, on='Emp_ID', how='left')

print("=== LEFT MERGE (Keep all Freelancers) ===")
print(left_merged)
print("\n" + "="*40 + "\n")

# -------------------------------------------------------------
# 3. Merging when column names don't match
# -------------------------------------------------------------
# Let's rename the column in the invoices table to simulate a messy client
invoices_messy = invoices.rename(columns={'Emp_ID': 'Freelancer_ID'})

# Instead of 'on', we explicitly define the left and right column names
mismatched_merge = pd.merge(
    freelancers, 
    invoices_messy, 
    left_on='Emp_ID', 
    right_on='Freelancer_ID', 
    how='inner'
)

print("=== MERGED WITH DIFFERENT COLUMN NAMES ===")
print(mismatched_merge)

# Merge them, then immediately drop the redundant column from the right table
clean_merge = pd.merge(
    freelancers, 
    invoices_messy, 
    left_on='Emp_ID', 
    right_on='Freelancer_ID', 
    how='inner'
).drop(columns=['Freelancer_ID'])
print("\n=== CLEAN MERGE (Dropped Redundant Column) ===")
print(clean_merge)