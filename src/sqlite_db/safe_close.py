import sqlite3


# Cách 1: sử dụng try - catch - finally
conn = sqlite3.connect("safe_close.db")
try:
    with conn:
        # Thực hiện các thao tác với cơ sở dữ liệu ở đây
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)"
        )
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()

# Kiểm tra xem kết nối đã được đóng hay chưa
try:
    conn.execute("SELECT * FROM users")
except sqlite3.ProgrammingError as e:
    print(f"An error occurred: {e}")   # nếu đã đóng thì sẽ báo lỗi



# Cách 2: sử dụng context manager
from contextlib import closing

with closing(sqlite3.connect("safe_close.db")) as conn:
    with conn:
        # Thực hiện các thao tác với cơ sở dữ liệu ở đây
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)"
        )
        conn.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
        conn.execute("INSERT INTO users (name) VALUES (?)", ("Bob",))
        conn.execute("INSERT INTO users (name) VALUES (?)", ("Charlie",))

    # Kiểm tra dữ liệu trong bảng
    rows = conn.execute("SELECT * FROM users").fetchall()
    for row in rows:
        print(row)

# Kiểm tra xem kết nối đã được đóng hay chưa
try:
    conn.execute("SELECT * FROM users")
except sqlite3.ProgrammingError as e:
    print(f"An error occurred: {e}")
