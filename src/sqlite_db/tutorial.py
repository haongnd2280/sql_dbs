import sqlite3


# Create a database connection and a cursor
conn = sqlite3.connect("tutorial.db")
cursor = conn.cursor()

# Create a table using flexible typing feature of SQLite
cursor.execute(
    "CREATE TABLE IF NOT EXISTS movies(title, year, score)"
)

# Verify that the table was created successfully by querying
# the sqlite_master table (built-in in SQLite), which contains
# information about all tables in the database
result = cursor.execute(
    "SELECT name FROM sqlite_master"
)
print(result.fetchall())

# Nếu ta query sqlite_master với table 'spam' không tồn tại thì res.fetchone() sẽ trả về None
result = cursor.execute(
    "SELECT name FROM sqlite_master WHERE name='spam'"
)
print(result.fetchall())    # return an empty list

# Add two rows of data to the table using SQL literals
cursor.execute(
    """INSERT INTO movies VALUES
            ("Monty Python and the Holy Grail", 1975, 8.2),
            ("And Now for Something Completely Different", 1971, 7.5)
    """
)
conn.commit()  # Commit the changes to the database

# We can verify that the data was inserted correctly by executing a SELECT query.
result = cursor.execute(
    "SELECT score FROM movies"
)
print(result.fetchall())


# Now, insert three more rows by calling cur.executemany(...):
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cursor.executemany("INSERT INTO movies VALUES (?, ?, ?)", data)
conn.commit()  # Remember to commit the transaction after executing INSERT

# Verify that the new rows were inserted by executing a SELECT query,
# this time iterating over the results of the query:
rows = cursor.execute(
    """SELECT year, title FROM movies
    ORDER BY year"""
)
for row in rows:
    print(row)


# Finally, verify that the database has been written to disk by calling con.close()
# to close the existing connection, opening a new one, creating a new cursor, then querying the database
conn.close()

new_conn = sqlite3.connect("tutorial.db")
new_cursor = new_conn.cursor()

result = new_cursor.execute(
    "SELECT title, year FROM movies ORDER BY score DESC"
)
title, year = result.fetchone()
print(f"The highest scoring Monty Python movie is {title!r}, released in {year}")

new_conn.close()