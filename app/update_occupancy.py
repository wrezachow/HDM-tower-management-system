import sqlite3

connection =sqlite3.connect('data/tower.db')

cursor = connection.cursor()

user_input = int(input("What would you like to do today?\n" \
"1. Update\n" \
"2. Add\n" \
"3. Remove\n" \
"\n" \
"Type choice number: "))

mng_choices = ['Update', 'Add', 'Remove']

user_input = mng_choices[user_input - 1]

all_units = ['A2', 'B2', 'C2', 'D2', 
                    'A3', 'C3', 
                    'A4', 'C4', 
                    'A5', 'B5', 'C5', 'D5', 
                    'A6', 'B6', 'C6', 
                    'A7', 'B7', 'C7', 
                    'A8', 'B8', 'C8', 
                    'A9', 'B9', 'C9', 
                    'A10', 'B10', 'C10', 'D10', 
                    'A11', 'B11', 'C11', 'D11', 
                    'A12', 'B12', 
                    'A13', 'B13', 'D3-D4', 'B3-B4', 'D6-D7', 'D8-D9', 'C12-D12', 'C13-D13']



def update_occupancy(unit_no, occupancy_status):
    data = [occupancy_status, unit_no]
    cursor.execute('UPDATE units SET occupancy_status=? WHERE unit_no=?',data)
    connection.commit()

    

if user_input == 'Update':
    unit_no = input('Which unit would you like to update?\n')
    if unit_no in all_units:
        occupancy_status = int(input('What would you like for status to be changed to?\n '
        '1. Owner\n ' \
        '2. Tenant\n ' \
        '3. None\n' \
        '\n' \
        'Type the number: '))
    
    occupancy_choices = ['Owner', 'Tenant', 'None']
    occupancy_status = occupancy_choices[occupancy_status - 1]
    
    update_occupancy(unit_no, occupancy_status)