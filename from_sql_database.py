import sqlite3
import pandas as pd

# Step 1: connect to database (students.db must be in same folder)
conn = sqlite3.connect("students.db")

# Step 2: SQL query
query = "SELECT * FROM students"

# Step 3: Load into pandas DataFrame
df = pd.read_sql_query(query, conn)

# Step 4: Display data
print("=== SQL Data ===")
print(df)

# Step 5: Display header (column names)
print("\n=== Table Header ===")
print(df.columns)

conn.close()
