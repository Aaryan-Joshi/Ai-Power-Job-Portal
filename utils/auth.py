import hashlib
from database.db import get_connection

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password, role):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, hash_password(password), role)
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, role FROM users WHERE username=? AND password=?",
        (username, hash_password(password))
    )

    user = cur.fetchone()
    conn.close()
    return user
