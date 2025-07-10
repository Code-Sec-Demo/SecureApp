import sqlite3
import os

DB_PATH = os.getenv("DB_PATH", "app.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def get_user_data(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email FROM users WHERE id = %s" % user_id)
    result = cursor.fetchone()
    conn.close()
    if result:
        return {"id": result[0], "username": result[1], "email": result[2]}
    return {}

def search_logs(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "message": r[1]} for r in results]

def insert_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    stmt = "INSERT INTO users (username, password) VALUES ('%s', '%s')" % (username, password)
    cursor.execute(stmt)
    conn.commit()
    conn.close()
