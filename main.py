import sqlite3

def init_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER)
    ''')
    return conn

def add_user(conn, name, age):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
    conn.commit()

def get_users(conn, name):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM users WHERE name=?''', (name,))
    return cursor.fetchone()
