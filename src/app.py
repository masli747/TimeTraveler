"""
 * app.py contains the view code to drive the user's view of the database, and 
 * calls the controller in order to execute the user's desired modifications
 * to the database.
"""

# Library imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Local DB imports
from controller import controller

ctrl_obj = None

def init():
    global ctrl_obj

    if ctrl_obj is None:
        ctrl_obj = controller()

def on_closing():
    global ctrl_obj

    ctrl_obj.destructor()

def dummy_too():
    return ctrl_obj.dummy_function()

def dummy_three():
    print("Hello again, world!")

def build_add_view(parent):
    global ctrl_obj

    # Notebook containing subviews that we will return
    insert_notebook = ttk.Notebook(parent)

    # View for adding Trips
    add_trip_view = ttk.Frame(insert_notebook)

    test = Label(add_trip_view, text=dummy_too())    
    test.pack()

    # View for adding Travelers
    add_traveler_view = ttk.Frame(insert_notebook)

    # View for adding Companions
    add_companion_view = ttk.Frame(insert_notebook)
    build_add_companion_frame(add_companion_view)

    # View for adding Vehicles
    add_vehicle_view = ttk.Frame(insert_notebook)

    # View for adding Tools
    add_tool_view = ttk.Frame(insert_notebook)

    # Add all views to the notebook
    insert_notebook.add(add_trip_view, text='Add Trip')
    insert_notebook.add(add_traveler_view, text="Add Traveler")
    insert_notebook.add(add_companion_view, text="Add Companion")
    insert_notebook.add(add_vehicle_view, text="Add Vehicle")
    insert_notebook.add(add_tool_view, text="Add Tool")

    return insert_notebook

def build_add_companion_frame(add_companion_view):
    # Labels for all Companion Attributes
    name_label = Label(add_companion_view, text="Name:")
    age_lable = Label(add_companion_view, text="Age:")
    location_lable = Label(add_companion_view, text="Original Location:")
    traveler_lable = Label(add_companion_view, text="Travels With:")
    name_label.grid(row = 0, column = 0, sticky = W, padx = 2, pady = 2)
    age_lable.grid(row = 1, column = 0, sticky = W, padx = 2, pady = 2)
    location_lable.grid(row = 2, column = 0, sticky = W, padx = 2, pady = 2)
    traveler_lable.grid(row = 3, column = 0, sticky = W, padx = 2, pady = 2)
    
    # Strings and Entry widgets for all Companion Attributes
    name_string = StringVar()
    age_string = StringVar()
    location_string = StringVar()
    valid_travelers = ctrl_obj.select_all("Travelers", False)
    name_entry = Entry(add_companion_view, textvariable=name_string)
    age_entry = Entry(add_companion_view, textvariable=age_string)
    location_entry = Entry(add_companion_view, textvariable=location_string)
    traveler_combo = ttk.Combobox(add_companion_view, values=valid_travelers, state="readonly")
    name_entry.grid(row = 0, column = 1, pady = 2)
    age_entry.grid(row = 1, column = 1, pady = 2)
    location_entry.grid(row = 2, column = 1, pady = 2)
    traveler_combo.grid(row = 3, column = 1, pady = 2)
    
    # Button to submit all attributes to controller for insertion.
    submission_button = Button(add_companion_view, text="Add", command=lambda: submit_companion(
        name_string.get(), 
        age_string.get(), 
        location_string.get(), 
        traveler_combo.get()))
    submission_button.grid(row = 4, column = 2, sticky = S, padx = 2, pady = 2)

def submit_companion(name, age, location, traveler):
    # Make sure the user wants to insert a companion.
    insert = add_confirmation("Companion")
    
    # Break out early if not returning
    if not insert:
        return
    
    # Check user input for errors
    try:
        temp = traveler[0]
        if name == "" or age == "" or location == "": 
            raise ValueError
        # print(name, age, location, traveler[0] if traveler[0] != None else "")
    except IndexError:
        messagebox.showinfo(message='Error: Selected traveler companion is invalid!')
        return
    except:
        messagebox.showinfo(message='Error: Entered companion values are incorrect!')
        return

    # if user wants to insert, add the companion into our db using controller.
    if insert:
        ctrl_obj.insert_companion(name, age, location, traveler[0])
        messagebox.showinfo(message='Companion added!')
        return
    else:
        return

def add_confirmation(message):
    return messagebox.askyesno(message=f'Are you sure you want to add this {message}?',
                                 icon='question',
                                 title='Add Confirmation')

# Main builds/arranges all basic UI elements and tells tkinter to run the program.
def main():
    # Get our reference to the controller
    init()

    # Define the root window.
    root = Tk()
    root.title("The Time Traveler's Database")
    root.geometry("960x720")

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