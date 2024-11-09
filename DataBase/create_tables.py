import sqlite3

connection = sqlite3.connect('DataBase\\data_base.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS refill (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime TEXT NOT NULL,
    count REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS cost (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime TEXT NOT NULL,
    count REAL NOT NULL,
    category INTEGER ,
    FOREIGN KEY (category) REFERENCES categories(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

connection.close()
