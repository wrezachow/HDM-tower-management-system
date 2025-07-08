import sqlite3

connection =sqlite3.connect('data/tower.db')

cursor = connection.cursor()

print('To view the table ''units'' type the 3-digit pin: ')

pin = '6532'

