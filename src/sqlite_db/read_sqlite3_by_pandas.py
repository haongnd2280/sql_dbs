import sqlite3
import pandas as pd


conn = sqlite3.connect("example.db")

# Read a table into a DataFrame
df = pd.read_sql(sql="SELECT * FROM users", con=conn)
print(df)

conn.close()
