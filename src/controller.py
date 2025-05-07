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
    
    def insert_companion(self, name, age, location, travelerID):
        query = '''INSERT INTO Companion (name, age, originalLocation, travelerID)
VALUES (%s, %s, %s, %s);'''

        self.db_ops.modify_query_params(query, (name, age, location, travelerID))
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
                case "trip":
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

        query = f'''SELECT {attributes} FROM {target_table};'''

        return self.db_ops.select_query(query)
        
    def dummy_function(self):
        return "Hello, World!"
    
    def destructor(self):
        self.db_ops.destructor()
        return