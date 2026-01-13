import sqlite3

DB_NAME = "database/ats.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def init_db():
    conn = get_connection()
    with open("database/schema.sql") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
