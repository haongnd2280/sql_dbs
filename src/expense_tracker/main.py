# 🧾 Use Case: Expense Tracker
# You're building a personal finance app that:

# Records daily expenses
# Categorizes them (Food, Transport, etc.)
# Lets you view total spent by category

import sqlite3
from datetime import date

# Connect to / create a db file
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Create a table to store expenses
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        note TEXT,
        date TEXT DEFAULT CURRENT_DATE
    )
"""
)
conn.commit()


# Add an expense
def add_expense(amount: float, category: str, note: str = "") -> None:
    today = date.today().isoformat()
    cursor.execute(
        "INSERT INTO expenses (amount, category, note, date) VALUES (?, ?, ?, ?)",
        (amount, category, note, today)
    )
    conn.commit()


# View Total Spent by Category
def view_total_by_category() -> None:
    cursor.execute("""
        SELECT category,
        SUM(amount) FROM expenses
        GROUP BY category
    """)
    rows = cursor.fetchall()
    for category, total in rows:
        print(f"{category}: ${total:.2f}")


# View all expenses
def list_expenses() -> None:
    cursor.execute("""
        SELECT date, category, amount, note FROM expenses
        ORDER BY date DESC
    """)
    rows = cursor.fetchall()
    for date, category, amount, note in rows:
        print(f"{date} | {category:<10} | ${amount:.2f} | {note}")


if __name__ == "__main__":
    add_expense(12.50, "Food", "Lunch")
    add_expense(3.20, "Transport", "Bus fare")
    add_expense(45.00, "Groceries", "Weekly shop")

    print("All Expenses:")
    list_expenses()

    print("\nTotal by Category:")
    view_total_by_category()
    conn.close()
