import sqlite3


# Open database in read-only mode
conn = sqlite3.connect(database="file:tutorial.db?mode=ro", uri=True)
try:
    with conn:
        conn.execute("CREATE TABLE movies(title, year, score)")
except sqlite3.OperationalError as e:
    print(f"Error: {e}")
finally:
    conn.close()


# Do not implicitly create a new database file if it does not already exist; 
# will raise OperationalError if unable to create a new file
try:
    conn = sqlite3.connect(database="file:nosuchdb.db?mode=rw", uri=True)
except sqlite3.OperationalError as e:
    print(f"Error: {e}")
finally:
    conn.close()
