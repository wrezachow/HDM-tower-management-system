import sqlite3

connection = sqlite3.connect('data/tower.db')

cursor = connection.cursor()

def add_occupant(unit_no, occupied_by, phone, occupant_status):
    data = [unit_no, occupied_by, phone]

    #checks for occupancy status
    cursor.execute('SELECT occupancy_status FROM units WHERE unit_no=?',(unit_no,))
    
    #Fetches occupancy status
    occupancy_status = cursor.fetchone()

    if occupancy_status is None:
        print(f'The Unit {unit_no} does not exist')
        pass
    else:
        occupancy_status = occupancy_status[0]

    #Condition for empty unit
    if occupancy_status == 'None': 
        cursor.execute('INSERT INTO occupants (unit_no, occupied_by, phone) VALUES (?,?,?)',data)
        print(f'Successfully added {occupied_by} to Unit {unit_no}')
        cursor.execute('UPDATE units SET occupancy_status=? WHERE unit_no=?',(occupant_status, unit_no,))

    #if there is an existing occupant
    elif occupancy_status == 'Tenant':
        print('Unit currently occupied by occupant')

    #if there is an Owner occupying unit
    elif occupancy_status == 'Owner':
        print('Unit is Owner occupied')
    
    connection.commit()


def view_occupants(unit_no=None):
    if unit_no:
        cursor.execute('SELECT * FROM occupants WHERE unit_no=?',(unit_no,))
    else:
        cursor.execute('SELECT * FROM occupants')

    occupants = cursor.fetchall()
    for occupant in occupants:
        print(occupant)

def edit_phone(phone, unit_no):
    data = [phone, unit_no]

    cursor.execute('SELECT * FROM occupants WHERE unit_no=?',(unit_no,))
    occupant = cursor.fetchone()

    if occupant is None:
        print("No occupant found with that phone number.")
    else:
        cursor.execute('UPDATE occupants SET phone=? WHERE unit_no=?',data)
        connection.commit()
        print('The occupant''s  phone number been updated successfully.')

    

def edit_name(name, phone):
    data = [name, phone]
    cursor.execute('SELECT * FROM occupants WHERE phone=?',(phone,))
    occupant = cursor.fetchone()

    if occupant is None:
        print("No occupant found with that phone number.")
    else:
        cursor.execute('UPDATE occupants SET occupied_by=? WHERE phone=?',data)
        connection.commit()
        print('The occupant''s name has been updated successfully.')

def edit_occupant_info():
    user_input = input('What would you like to edit?\n' \
    '1. Phone Number' \
    '2. Name\n' \
    '\n' \
    'Type the number of what you want to edit: ').strip()

    if user_input == '1':
        unit_no = input('What unit does the occupant reside in?\n')
        phone = input('Please provide new phone number: ')
        
        edit_phone(phone, unit_no)
    
    elif user_input == '2':
        phone = input('Provide occupant''s Phone number: ' )
        name = input('What is occupant''s new name?\n')

        edit_name(name, phone)



def del_occupant(unit_no):
    cursor.execute('DELETE FROM occupants WHERE unit_no=?',(unit_no,))
    cursor.execute('UPDATE units SET occupancy_status=? WHERE unit_no=?',('None', unit_no,))
    connection.commit()
    print('Deleted')

if __name__ == '__main__':
#Main Program for ability to use all functions

