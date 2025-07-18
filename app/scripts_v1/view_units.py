import sqlite3

connection =sqlite3.connect('data/tower.db')

cursor = connection.cursor()

def show_units():
    cursor.execute("SELECT * FROM units")
    units = cursor.fetchall()

    for unit in units:
        print(unit)