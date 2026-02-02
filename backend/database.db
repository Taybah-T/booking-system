import sqlite3

db = sqlite3.connect("database.db")

db.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT,
    lname TEXT,
    email TEXT UNIQUE,
    password TEXT
);
""")

db.commit()
db.close()

print("Database created!")