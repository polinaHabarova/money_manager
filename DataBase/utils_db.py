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


def get_refill():
    connection, cursor = create_connection()
    try:
        cursor.execute("SELECT SUM(count) FROM refill")
        result = cursor.fetchone()
        result = result[0]
    finally:
        connection.close()
    return result

def get_cost():
    connection, cursor = create_connection()
    try:
        cursor.execute("SELECT SUM(count) FROM cost")
        result = cursor.fetchone()
        result = result[0]
    finally:
        connection.close()
    return result

def get_allData():
    connection, cursor = create_connection()
    try:
        cursor.execute("SELECT * FROM refill")
        result1 = cursor.fetchall()
        cursor.execute("SELECT * FROM cost")
        result2 = cursor.fetchall()
    finally:
        connection.close()
    return result1, result2

def delete_data(id, color):
    connection, cursor = create_connection()
    try:
        if color == 'green':
            cursor.execute("DELETE FROM refill WHERE id=?",(id,))
            connection.commit()
        else:
            cursor.execute("DELETE FROM cost WHERE id=?", (id,))
            connection.commit()
    finally:
        connection.close()
