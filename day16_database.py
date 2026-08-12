import sqlite3

print("1. Connecting to the database...")
# This creates a file named 'scraped_leads.db' on your Mac
conn = sqlite3.connect("scraped_leads.db")

# The cursor is the tool we use to send SQL commands to the database
cursor = conn.cursor()

print("2. Creating the 'contacts' table...")

# ADD THIS LINE: It completely deletes the table if it already exists
cursor.execute('DROP TABLE IF EXISTS contacts')

cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    company TEXT,
    email TEXT
)
''')

print("3. Injecting scraped data...")
scraped_data = [
    ("Alice Smith", "TechCorp", "alice@techcorp.com"),
    ("Bob Jones", "DataInc", "bob@datainc.com")
]

# The question marks (?) protect the database from formatting errors and hacks
cursor.executemany("INSERT INTO contacts (name, company, email) VALUES (?, ?, ?)", scraped_data)

# You MUST commit the changes, otherwise they won't be saved!
conn.commit()

print("4. Retrieving data from the database:")
cursor.execute("SELECT * FROM contacts")

# Fetch all the results and print them row by row
rows = cursor.fetchall()
for row in rows:
    print(f" - {row}")

# Always close the connection when you are done
conn.close()