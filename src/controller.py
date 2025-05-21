"""
 * Controller contains methods to allow the user to interact with the model (MySQL Server)
 * The Controller also handles returning data to the view for display. Interactions
 * with the model are handled by a helper class, db_operations.
"""

from db_operations import db_operations

class controller:
    def __init__(self):
        self.db_ops = db_operations()
        return
    
    def insert_trip(self, location, image, travelerID):
        query = '''INSERT INTO Trip (location, imageFile, travelerID)
VALUES (%s, %s, %s);''' 
        # COMMIT; isn't necessary since it's added by cursor.commit() in the db_operations file.

        self.db_ops.modify_query_params(query, (location, image, travelerID))
        return
    
    def insert_traveler(self, name, age, location):
        query = '''INSERT INTO Traveler (name, age, birthLocation)
VALUES (%s, %s, %s)'''

        self.db_ops.modify_query_params(query, (name, age, location))
        return
    
    def insert_companion(self, name, age, location, travelerID):
        query = '''INSERT INTO Companion (name, age, originalLocation, travelerID)
VALUES (%s, %s, %s, %s);'''

        self.db_ops.modify_query_params(query, (name, age, location, travelerID))
        return
    
    def insert_vehicle(self, name, power_capacity, engine, travelerID):
        query = '''INSERT INTO Vehicle (name, powerCapacity, engine, travelerID)
VALUES (%s, %s, %s, %s)'''

        self.db_ops.modify_query_params(query, (name, power_capacity, engine, travelerID))
        return

    def insert_tool(self, name, power_capacity, travelerID):
        query = '''INSERT INTO Tool (name, powerCapacity, travelerID)
VALUES (%s, %s, %s)'''

        self.db_ops.modify_query_params(query, (name, power_capacity, travelerID))
        return
    
    def select_all(self, type, verbose):
        type = type.lower()

        try:
            match type:
                case "travelers":
                    target_table = "Traveler"
                case "companions":
                    target_table = "Companion"
                case "vehicles":
                    target_table = "Vehicle"
                case "trips":
                    target_table = "Trip"
                case "tools":
                    target_table = "Tool"
                case _:
                    raise ValueError("Invalid Table Selection!") 
        except Exception as e:
            print(e)

        if verbose:
            attributes = "*"
        else:
            match type:
                case "travelers":
                    attributes = "travelerID, name"
                case "companions":
                    attributes = "companionID, name"
                case _:
                    attributes = "*"

        query = f'''SELECT {attributes} FROM {target_table};'''

        return self.db_ops.select_query(query)
    
    def get_count(self, table, attribute):
        query = f'''SELECT COUNT({attribute}) AS result
FROM {table}'''

        return self.db_ops.select_query(query)

    def get_average(self, table, attribute, group):
        query = f'''SELECT AVG({attribute}) AS result
FROM {table}'''

        if group != None:
            query += f'''\nGROUP BY {group};'''
            return self.db_ops.select_query(query)
        else:
            query += ''';'''
            return self.db_ops.select_query(query)
    
    def get_average_trips(self, type):
        # Python f-string because connector %s substitution doesn't work with subqueries.
        query = f'''SELECT AVG(trip_count) AS average_number_trips
FROM
    (
        SELECT COUNT(*) AS trip_count
        FROM v_master_records
        GROUP BY {type}
    ) AS trips;'''
        
        return self.db_ops.select_query(query)

    def get_column_names(self, table):
        query = f'''SELECT * FROM {table}'''

        return self.db_ops.return_column_names(query)
    
    def generate_report(self):
        query = '''SELECT * FROM v_master_records;'''

        return self.db_ops.select_query(query)

    def destructor(self):
        self.db_ops.destructor()
        return