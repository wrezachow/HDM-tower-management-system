import sqlite3

connection =sqlite3.connect('data/tower.db')

cursor = connection.cursor()

pin_input = input('To view the table ''units'' type the 3-digit pin: ')

pin_units = '6532'

if pin_input == pin_units:
    cursor.execute("SELECT * FROM units")
    units = cursor.fetchall()

    for unit in units:
        print(unit)