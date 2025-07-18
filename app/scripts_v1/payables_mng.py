import sqlite3
from datetime import datetime


connection = sqlite3.connect('data/tower.db')

cursor = connection.cursor()

def validate_month(month):

    try:
        datetime.strptime(month, '%m-%Y')
        return True
    
    except ValueError:
        
        return False
    
def validate_unit(unit_no):
    units = cursor.execute("SELECT unit_no FROM units").fetchall()

    for unit in units:
        if unit_no == unit[0]:
            return True
            
    return False

def add_payable(unit_no, month, paid='No'):
    service_charge = 0

    
    if validate_month(month):
        #checks for occupancy status
        cursor.execute('SELECT occupancy_status FROM units WHERE unit_no=?',(unit_no,))
        
        #Fetches occupancy status
        occupancy_status = cursor.fetchone()

        if occupancy_status is None:
            print(f'The Unit {unit_no} does not exist')
            return
        
        else:
            occupancy_status = occupancy_status[0]

        #checks for unit type
        cursor.execute('SELECT unit_type FROM units WHERE unit_no=?',(unit_no,))
        unit_type = cursor.fetchone()

        if unit_type is None:
            print(f'The unit_type {unit_type} does not exist.')
            pass
        else:
            unit_type = unit_type[0]

        
        #Condition for empty unit 0 service charge
        if occupancy_status == 'None':
            print("No payables, flat unoccupied")
            return   

        if unit_type == 'Duplex':
            service_charge = 7000
        else:
            service_charge = 5000

        data = [unit_no, month, service_charge, paid]

        cursor.execute('INSERT INTO payables (unit_no, month, service_charge, paid) VALUES (?,?,?,?)',data)

    
    connection.commit()

def view_payables(unit_no=None, month=None):
    print("What would you like to do?\n"
    "1. Show All Payables\n"
    "2. Filter by month\n"
    "3. Filter by unit_no\n"
    "4. Filter by both unit_no and month")

    choice = input("Choices (1-4): ") 

    if choice == '1':
        payables = cursor.execute('SELECT * FROM payables').fetchall()

    elif choice == '2':
        month = input('Enter month (MM-YYYY): ')
        if validate_month(month):
            payables = cursor.execute('SELECT * FROM payables WHERE month=?', (month,)).fetchall()

    elif choice == '3':
        unit_no = input('Enter Unit No: ')
        if validate_unit(unit_no):
            payables = cursor.execute('SELECT * FROM payables WHERE unit_no=?', (unit_no,)).fetchall()

    elif choice == '4':
        month = input('Enter month (MM-YYYY): ')

        if validate_month(month):
            unit_no = input('Enter Unit No (Example: A2 or for Duplex B3-B4): ')
            payables = cursor.execute('SELECT * FROM payables WHERE unit_no=? AND month=?', (unit_no, month)).fetchall()
        else:
            print('Invalid month')

    else:
        print("Invalid option")
        return

    for payable in payables:
        print(payable)

def mark_as_paid(unit_no, month):
    if validate_unit(unit_no) and validate_month(month):
        cursor.execute('UPDATE payables SET paid=? WHERE paid=? AND unit_no=? AND month=?',('Yes','No',unit_no,month,))
        connection.commit()
        print(f'Service charge for unit {unit_no} has successfully been paid for {month}.')
    else:
        print(f'Invalid Entry')

def auto_add_payables(month):
    occupied_units = cursor.execute('SELECT unit_no FROM units WHERE occupancy_status=? OR occupancy_status=?',('Tenant','Owner',)).fetchall()
    unit_payables = cursor.execute('SELECT unit_no FROM payables').fetchall()

    unit_payablesL = []
    for unit_p in unit_payables:
        unit_payablesL.append(unit_p[0])

    for unit in occupied_units:
        unit = unit[0]


        if unit not in unit_payablesL:
            add_payable(unit, month)
            print(f'Added Unit {unit} to payables database')
        else:
            print(f'Unit {unit} is already in payables database')

# To-Dp for Day 4:
# 1. Improve view_payables():
#    - Validate month format (use validate_month)
#    - Sanitize unit_no input (maybe check if unit exists before querying)
#    - Add summary output (e.g., total due per view?)
#
# 2. Add mark_as_paid(unit_no, month):
#    - This function should:
#        a. Check if record exists for (unit_no, month)
#        b. If exists, UPDATE payables SET paid='Yes'
#        c. Confirm update with user

