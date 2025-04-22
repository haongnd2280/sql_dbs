import sqlite3


conn = sqlite3.connect(":memory:")

# Create a table
conn.execute("CREATE TABLE language(name, first_appeared)")     # This returns Cursor object

# Insert many data simultaneously
data = [
    ("C++", 1985),
    ("Objective-C", 1984),
]
conn.executemany(
    "INSERT INTO language(name, first_appeared) VALUES(?, ?)",
    data,
)

# Print the table content
rows = conn.execute("SELECT * FROM language")
for row in rows:
    print(row)


# Delete rows
row_count = conn.execute("DELETE FROM language").rowcount
print(f"I just deleted {row_count} rows")

# Check the remaining rows
cursor = conn.execute("SELECT * FROM language")
rows = cursor.fetchall()
print(f"The number of rows left: {len(rows)}")

# close() is not a shortcut method and it's not called automatically;
# the connection object should be closed manually
conn.close()
