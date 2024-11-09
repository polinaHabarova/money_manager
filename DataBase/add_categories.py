import sqlite3

connection = sqlite3.connect('DataBase\\data_base.db')
cursor = connection.cursor()
def add_categories(name):
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
    connection.commit()

add_categories('Развлечения')
add_categories('Образование')
add_categories('Еда')
add_categories('Прочее')
connection.close()