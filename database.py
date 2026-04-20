import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserName TEXT NOT NULL,
        Email TEXT UNIQUE NOT NULL,
        Password TEXT NOT NULL)
    """)

cur.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    event_date TEXT NOT NULL)
    """)



print("Database created!")