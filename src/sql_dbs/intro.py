import sqlite3

# Create / connect to a database file
connection = sqlite3.connect("example.db")
# You can also use an in-memory database (does not persist):
# connection = sqlite3.connect(":memory:")

# A cursor allows you to execute SQL commands.
cursor = connection.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
"""
)

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
connection.commit()  # Don"t forget to save changes

# Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
connection.close()
