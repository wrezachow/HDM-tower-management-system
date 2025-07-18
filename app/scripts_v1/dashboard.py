import sqlite3
from datetime import datetime
from app.scripts_v1.payables_mng import view_payables, add_payable, mark_as_paid, auto_add_payables, validate_month, validate_unit
from app.scripts_v1.occupant_mng import view_occupants, edit_occupant_info, del_occupant

connection = sqlite3.connect('data/tower.db')
cursor = connection.cursor()

def show_dashboard():
    #count units that have to pay service charge
    #count units that paid service charge
    month = datetime.today().strftime("%m-%Y")
    
    if validate_month(month):
        total_units = cursor.execute('SELECT COUNT(*) FROM units').fetchone()[0]
        tenant_occupied = cursor.execute('SELECT COUNT(*) FROM units WHERE occupancy_status=?',('Tenant',)).fetchone()[0]
        owner_occupied = cursor.execute('SELECT COUNT(*) FROM units WHERE occupancy_status=?',('Owner',)).fetchone()[0]
        occupied_units = tenant_occupied + owner_occupied
        empty_units = total_units - occupied_units


        unpaid_units = cursor.execute('SELECT COUNT(*) FROM payables WHERE paid=?',('No',)).fetchone()[0]
        paid_units = cursor.execute('SELECT COUNT(*) FROM payables WHERE paid=?',('Yes',)).fetchone()[0]

    print('-' * 50)
    print("Welcome to Hajee Dudu Meah Tower Management System!")
    print('-' * 50)
    print(f'Month: {month}')
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
    print()
    print('-' * 50)

'''
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
    
'''





