import sqlite3

def main():
    connection = sqlite3.connect("data/tower.db")
    cursor = connection.cursor()

    single_units = ['A2', 'B2', 'C2', 'D2', 
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
                    'A13', 'B13']

    duplex_units = ['D3-D4', 'B3-B4', 'D6-D7', 'D8-D9', 'C12-D12', 'C13-D13']

    for unit in single_units:
        unit_type = 'Single'
        occupancy_status = 'None'

        if len(unit) < 3:
            floor = int(unit[1])
        else:
            floor = int(unit[1:])
        
        data = [unit, unit_type, occupancy_status, floor]
        cursor.execute("INSERT INTO 'units' ('unit_no','unit_type','occupancy_status','floor') VALUES (?,?,?,?)",data)
        

    for unit in duplex_units:
        unit_type = 'Duplex'
        occupancy_status = 'None'

        floor = None
        
        data = [unit, unit_type, occupancy_status, floor]
        cursor.execute("INSERT INTO 'units' ('unit_no','unit_type','occupancy_status','floor') VALUES (?,?,?,?)",data)
    connection.commit()
    connection.close()    

if __name__ == "__main__":
    main()