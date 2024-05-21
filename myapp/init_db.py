import sqlite3

conn = sqlite3.connect('app.db')
c = conn.cursor()

c.execute('''CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)''')

conn.commit()
conn.close()
