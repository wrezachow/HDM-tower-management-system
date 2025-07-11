import sqlite3

connection =sqlite3.connect('data/tower.db')

cursor = connection.cursor()

cursor.execute("SELECT * FROM units")
units = cursor.fetchall()

for unit in units:
    print(unit)