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
    
    def select_all(self, type):
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
                    raise ValueError("Invalid selection") 
        except Exception as e:
            print(e)

        query = f"""SELECT * FROM {target_table};"""

        return self.db_ops.select_query(query)
        
    
    def destructor(self):
        self.db_ops.destructor()
        return