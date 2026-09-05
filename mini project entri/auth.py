import sqlite3

DB_NAME = "xyz.db"


def register():
    con = sqlite3.connect(DB_NAME)
    c = con.cursor()

    u = input("Enter username: ")
    p = input("Enter password: ")

    try:
        c.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (u, p)
        )

        con.commit()
        print("Registration successful!")

    except sqlite3.IntegrityError:
        print("Username already exists!")

    finally:
        con.close()


def login():
    con = sqlite3.connect(DB_NAME)
    c = con.cursor()

    u = input("Enter username: ")
    p = input("Enter password: ")

    c.execute(
        "SELECT id FROM users WHERE username = ? AND password = ?",
        (u, p)
    )

    x = c.fetchone()

    con.close()

    if x:
        print("Login successful!")
        return x[0]       # Return user's ID

    else:
        print("Login failed")
        return None