import sqlite3
from datetime import datetime
def create_connection():
    connection = sqlite3.connect('DataBase\\data_base.db')
    cursor = connection.cursor()
    return connection, cursor

def add_refill(count, datetime):
    connection, cursor = create_connection()
    try:
        cursor.execute("INSERT INTO refill (count, datetime) VALUES (?, ?)", (count, datetime))
        connection.commit()
    finally:
        connection.close()

def add_cost(count, datetime, name):
    connection, cursor = create_connection()
    try:
        cursor.execute("SELECT id FROM categories WHERE name=?", (name,))
        result = cursor.fetchone()
        result = result[0]
        cursor.execute("INSERT INTO cost (count, datetime, category) VALUES (?, ?, ?)", (count, datetime, result))
        connection.commit()
    finally:
        connection.close()