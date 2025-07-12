import sqlite3
from datetime import datetime
from payables_mng import view_payables, add_payable, mark_as_paid
from occupant_mng import view_occupants, edit_occupant_info, del_occupant

connection = sqlite3.connect('data/tower.db')
cursor = connection.cursor()

def show_dashboard():
    #uses total units for:
    #shows occupied units
    #shows empty units

    #show owner occupied
    #show Tenant occupied
    
    #count units that have to pay service charge
    #count units that paid service charge

    total_units = cursor.execute('SELECT COUNT(*) FROM units').fetchall()
    tenant_occupied = cursor.execute('SELECT COUNT(*) FROM units WHERE ocupancy_status=?',('Tenant',)).fetchall()
    owner_occupied = cursor.execute('SELECT COUNT(*) FROM units WHERE ocupancy_status=?',('Owner',)).fetchall()
    occupied_units = tenant_occupied + owner_occupied
    empty_units = total_units - occupied_units


    unpaid_units = cursor.execute('SELECT COUNT(*) FROM payables WHERE paid=?',('No',)).fetchall()
    paid_units = cursor.execute('SELECT COUNT(*) FROM payables WHERE paid=?',('Yes',)).fetchall()

    print("Welcome to Hajee Dudu Meah Tower Management System!")
    
    print(f"Units Available: {empty_units}")
    print(f"Units Occupied: {occupied_units}")
    print()
    print()
    print(f"Tenant Occupied Units: {tenant_occupied}")
    print(f"Owner Occupied Units: {owner_occupied}")
    print()
    print()
    print(f"Units that owe Service Charge: {unpaid_units}")
    print(f"Units that paid Service Charge: {paid_units}")

def main():
    #Deal with payables
    #Deal with occupants
    #more later
    #Exit

    show_dashboard()
    print('=' * 50)
    print()
    print()

    print('What would you like to do')
    







#if __name__ == '__main__':
