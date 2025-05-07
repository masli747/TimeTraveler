"""
 * app.py contains the view code to drive the user's view of the database, and 
 * calls the controller in order to execute the user's desired modifications
 * to the database.
"""

# Library imports
from tkinter import *
from tkinter import ttk

# Local DB imports
from controller import controller


def build_add_view(parent):
    # Notebook containing subviews that we will return
    insert_notebook = ttk.Notebook(parent)

    # View for adding Trips
    trip_view = ttk.Frame(insert_notebook)

    test = Label(trip_view, text="Add a trip")    
    test.pack()

    # View for adding Travelers

    # Add all views to the notebook
    insert_notebook.add(trip_view, text='Add Trip')
    
    return insert_notebook

# Main builds/arranges all basic UI elements and tells tkinter to run the program.
def main():
    # Define the root window.
    root = Tk()
    root.title("The Time Traveler's Database")
    root.geometry("600x400")

    # Make a notebook, so we can switch between views.
    root_notebook = ttk.Notebook(root)

    # Define the notebook's views.
    # First page (Adding).
    add_view = ttk.Frame(root_notebook)   

    # Widgets/elements for the first page.
    insert_views = build_add_view(add_view)
    insert_views.pack(fill="both", expand=True)

    # Second page (Editing).
    edit_view = ttk.Frame(root_notebook)  

    # Widgets/elements for the second page.

    # Third page (viewing).
    database_view = ttk.Frame(root_notebook)

    # Fourth page (exporting/reports).
    export_view = ttk.Frame(root_notebook)

    # Add pages to the notebook.
    root_notebook.add(add_view, text='Add')
    root_notebook.add(edit_view, text='Edit')
    root_notebook.add(database_view, text="View")
    root_notebook.add(export_view, text="Export")

    # Put the notebook itself in the root view.
    root_notebook.pack(fill="both", expand=True)

    # Loop the program until the user quits.
    root.mainloop()

main()