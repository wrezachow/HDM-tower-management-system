import sqlite3
import datetime


connection = sqlite3.connect('data/tower.db')

cursor = connection.cursor()

def validate_month(month):

    try:
        datetime.strptime(month, '%m-%Y')
        return True
    
    except ValueError:
        
        return False
    

def add_payable(unit_no, month, electricity, paid='No'):
    service_charge = 0

    

    #checks for occupancy status
    cursor.execute('SELECT occupancy_status FROM units WHERE unit_no=?',(unit_no,))
    
    #Fetches occupancy status
    occupancy_status = cursor.fetchone()

    if occupancy_status is None:
        print(f'The Unit {unit_no} does not exist')
        pass
    
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
        pass    

    if unit_type == 'Duplex':
        service_charge = 7000
    else:
        service_charge = 5000

    data = [unit_no, month, service_charge, electricity, paid]

    cursor.execute('INSERT INTO payables (unit_no, month, service_charge, electricity, paid) VALUES (?,?,?,?,?)',data)

    
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
        payables = cursor.execute('SELECT * FROM payables WHERE month=?', (month,)).fetchall()

    elif choice == '3':
        unit_no = input('Enter Unit No: ')
        payables = cursor.execute('SELECT * FROM payables WHERE unit_no=?', (unit_no,)).fetchall()

    elif choice == '4':
        month = input('Enter month (MM-YYYY): ')
        unit_no = input('Enter Unit No: ')
        payables = cursor.execute('SELECT * FROM payables WHERE unit_no=? AND month=?', (unit_no, month)).fetchall()

    else:
        print("Invalid option")
        return

    for payable in payables:
        print(payable)

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


#if __name__ == '__main__':
