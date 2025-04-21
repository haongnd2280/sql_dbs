# 📘 Use Case: Simple Todo App (Command-Line)
# You want to build a to-do list that:
# Stores tasks in a database (so they persist)
# Lets users add, view, and mark tasks as done

import sqlite3

# Connect to / create the database
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# Create a table to store tasks
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        is_done INTEGER DEFAULT 0
    )
""")
conn.commit()


def add_task(description: str) -> None:
    cursor.execute(
        "INSERT INTO tasks (description) VALUES (?)",
        (description,)
    )
    conn.commit()


def list_tasks() -> None:
    cursor.execute(
        "SELECT id, description, is_done FROM tasks"
    )
    tasks = cursor.fetchall()
    for id, desc, done in tasks:
        status = "✅" if done else "❌"
        print(f"{id}: {desc} [{status}]")


def mark_done(task_id: int) -> None:
    cursor.execute(
        "UPDATE tasks SET is_done = 1 WHERE id = ?",
        (task_id,)
    )
    conn.commit()


if __name__ == "__main__":
    # Add tasks
    add_task("Learn Python")
    add_task("Study sqlite3 in Python")

    # List tasks
    print("All tasks:")
    list_tasks()

    # Mark a task as done
    task_id = 3
    mark_done(task_id)

    print(f"\nTasks after marking task {task_id} as done:")
    list_tasks()

    conn.close()
