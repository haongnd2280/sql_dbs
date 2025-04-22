# A Connection object can be used as a context manager that automatically commits / rolls back 
# open transactions when leaving the body of the context manager.

# Note: The connection object is not closed automatically when used as a context manager.

import sqlite3


conn = sqlite3.connect(":memory:")

# Create a table
conn.execute(
    """
    CREATE TABLE language(
        id INTEGER PRIMARY KEY,
        name VARCHAR UNIQUE
    )"""
)

# Successful, con.commit() is called automatically afterwards
with conn:
    conn.execute(
        "INSERT INTO language(name) VALUES (?)",
        ("Python",)
    )

# con.rollback() is called after the with block finishes with an exception,
# the exception is still raised and must be caught
try:
    with conn:
        conn.execute(
            "INSERT INTO language(name) VALUES (?)",
            ("Python",)
        )
except sqlite3.IntegrityError:
    print("Cound't add Python twice")   # because `name` is unique


# Connection object used as context manager only commits or rollbacks transactions,
# so the connection object should be closed manually
conn.close()
