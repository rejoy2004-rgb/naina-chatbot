import sqlite3

# Create database and tables
def create_database():

    conn = sqlite3.connect("naina.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Messages table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        role TEXT,
        content TEXT
    )
    """)

    conn.commit()
    conn.close()


# Save message
def save_message(user_id, role, content):

    conn = sqlite3.connect("naina.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages (user_id, role, content) VALUES (?, ?, ?)",
        (user_id, role, content)
    )

    conn.commit()
    conn.close()


# Load user messages
def load_messages(user_id):

    conn = sqlite3.connect("naina.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT role, content FROM messages WHERE user_id = ?",
        (user_id,)
    )

    rows = cursor.fetchall()
    conn.close()
    messages = []

    for row in rows:
        messages.append({
            "role": row[0],
            "content": row[1]
        })

    return messages