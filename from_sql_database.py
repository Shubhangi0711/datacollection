import sqlite3
import pandas as pd


conn = sqlite3.connect("students.db")


query = "SELECT * FROM students"


df = pd.read_sql_query(query, conn)


print(" SQL Data ")
print(df)


print("\nTable Header ")
print(df.columns)

conn.close()

