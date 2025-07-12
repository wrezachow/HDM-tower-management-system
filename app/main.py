import sqlite3
from datetime import datetime
from payables_mng import view_payables, add_payable, mark_as_paid, auto_add_payables, validate_month, validate_unit
from occupant_mng import add_occupant, view_occupants, edit_occupant_info, del_occupant, edit_name, edit_phone, update_occupancy
from dashboard import show_dashboard
from view_units import show_units

connection = sqlite3.connect('data/tower.db')
cursor = connection.cursor()

def main():
    while True:
        show_dashboard()
        
        print('1. View Payables')
        print('2. Auto Add Payables')
        print('3. Mark payable as paid')
        print('4. Show Occupants')
        print('5. Add Occupant') #Will plug update Occupancy status
        print('6. Edit Occupant Info')
        print('7. Delete Occupant')
        print('8. Show units')
        print('9. Exit')

        choice = input('Choices (1-9): ')
        
        if choice == '1':
            view_payables()

        elif choice == '2':
            month = input('Payable Month: ')
            if validate_month(month):
                auto_add_payables(month)

        elif choice == '3':
            unit_no = input("Unit: ")
            month = input("Month: ")
            if validate_unit(unit_no):
                if validate_month(month):
                    mark_as_paid(unit_no, month)

        elif choice == '4':
            f_choice = input("Do you want to check occupant of a specific unit? (y/n): ")
            if f_choice == 'y':
                unit_no = input('Unit: ')
                if validate_unit(unit_no):
                    view_occupants(unit_no)
            else:
                view_occupants()

        elif choice == '5':
            unit_no = input('Unit: ')
            occupied_by = input('Name: ')
            phone = input('Phone Number: ')
            occupant_status_c = input('1. Owner\n' \
            '2. Tenant\n'
            'Choices (1-2): ').strip()
            if occupant_status_c == '1':
                occupant_status = 'Owner'
            elif occupant_status_c == '2':
                occupant_status = 'Tenant'
            
            add_occupant(unit_no, occupied_by, phone, occupant_status)

        elif choice == '6':
            edit_occupant_info()
        elif choice == '7':
            unit_no = input('Unit: ')
            if validate_unit(unit_no):
                del_occupant(unit_no)

        elif choice == '8':
            show_units()
        elif choice == '9':
            break
        else:
            print('Please Try again')
        
        input('\nPress Enter to return to main menu...')

if __name__ == '__main__':
    main()
