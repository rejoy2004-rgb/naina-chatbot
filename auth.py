import sqlite3
# Signup function
def signup():

    conn = sqlite3.connect("naina.db")
    cursor = conn.cursor()

    print("\nSIGN UP")

    username = input("Create username: ")
    password = input("Create password: ")

    try:

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()

        print("\nAccount created successfully!")

    except:
        print("\nUsername already exists.")

    conn.close()


# Login function
def login():

    conn = sqlite3.connect("naina.db")
    cursor = conn.cursor()

    print("\nLOGIN")

    username = input("Username: ")
    password = input("Password: ")

    cursor.execute(
        "SELECT id FROM users WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        print("\nLogin successful!")
        return user[0]

    else:
        print("\nInvalid username or password.")
        return None