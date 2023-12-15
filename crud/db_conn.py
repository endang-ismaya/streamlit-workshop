import sqlite3

db_path = r"data/sqlite_db/todo_app.db"
conn = sqlite3.connect(db_path, check_same_thread=False)
c = conn.cursor()

# Database

# Table

# Field/Columns

# DataType


def create_table():
    # if not os.path.exists(db_path):
    c.execute(
        "CREATE TABLE IF NOT EXISTS todos("
        + "id INTEGER PRIMARY KEY AUTOINCREMENT, todo TEXT, todo_status TEXT,"
        + "todo_due DATE)"
    )


def add_todo(todo, todo_status, todo_due):
    c.execute(
        "INSERT INTO todos(todo, todo_status, todo_due) VALUES (?, ?, ?)",
        (todo, todo_status, todo_due),
    )
    conn.commit()


def update_todo(todo_id, todo, todo_status, todo_due) -> bool:
    try:
        c.execute(
            "UPDATE todos SET todo=?, todo_status=?, todo_due=? WHERE id=?",
            (todo, todo_status, todo_due, todo_id),
        )
        conn.commit()

        return True

    except Exception:
        return False


def delete_todo(todo_id) -> bool:
    try:
        c.execute("DELETE FROM todos WHERE id=?", (todo_id,))
        conn.commit()

        return True

    except Exception as err:
        print("delete_todo", str(err))
        return False


def view_all_data():
    c.execute("SELECT * FROM todos")
    data = c.fetchall()
    return data


def view_unique_todo():
    c.execute("SELECT id, todo FROM todos")
    data = c.fetchall()
    return data


def get_todo(todo_id):
    c.execute("SELECT * FROM todos WHERE id=?", (todo_id,))
    data = c.fetchall()
    return data
