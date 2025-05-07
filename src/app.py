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

def build_add_view(parent):
    global ctrl_obj

    # Notebook containing subviews that we will return
    insert_notebook = ttk.Notebook(parent)

    # Frames that will hold widgets in the notebook
    add_trip_view = ttk.Frame(insert_notebook)
    add_traveler_view = ttk.Frame(insert_notebook)
    add_companion_view = ttk.Frame(insert_notebook)
    add_vehicle_view = ttk.Frame(insert_notebook)
    add_tool_view = ttk.Frame(insert_notebook)

    # FIXME: Remove later!
    test = Label(add_trip_view, text="Inserting Trips")    
    test.pack()

    # Build each frame's widgets
    build_add_traveler_frame(add_traveler_view)
    build_add_companion_frame(add_companion_view)
    build_add_vehicle_frame(add_vehicle_view)
    build_add_tool_frame(add_tool_view)

    # Add all views to the notebook
    insert_notebook.add(add_trip_view, text='Trip')
    insert_notebook.add(add_traveler_view, text="Traveler")
    insert_notebook.add(add_companion_view, text="Companion")
    insert_notebook.add(add_vehicle_view, text="Vehicle")
    insert_notebook.add(add_tool_view, text="Tool")

    return insert_notebook

def build_add_traveler_frame(add_traveler_view):
    # Labels for all traveler Attributes
    name_label = Label(add_traveler_view, text="Name:")
    age_lable = Label(add_traveler_view, text="Age:")
    location_lable = Label(add_traveler_view, text="Original Location:")
    name_label.grid(row = 0, column = 0, sticky = W, padx = 4, pady = 2)
    age_lable.grid(row = 1, column = 0, sticky = W, padx = 4, pady = 2)
    location_lable.grid(row = 2, column = 0, sticky = W, padx = 4, pady = 2)

    # Strings and Entry widgets for all Companion Attributes
    name_string = StringVar()
    age_string = StringVar()
    location_string = StringVar()
    name_entry = Entry(add_traveler_view, textvariable=name_string)
    age_entry = Entry(add_traveler_view, textvariable=age_string)
    location_entry = Entry(add_traveler_view, textvariable=location_string)
    name_entry.grid(row = 0, column = 1, pady = 2)
    age_entry.grid(row = 1, column = 1, pady = 2)
    location_entry.grid(row = 2, column = 1, pady = 2)

    # Button to submit all attributes to controller for insertion.
    submission_button = Button(add_traveler_view, text="Add", command=lambda: submit_traveler(
        name_string.get(), 
        age_string.get(), 
        location_string.get()))
    submission_button.grid(row = 3, column = 2, sticky = S, padx = 2, pady = 2)

    return

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

    # Update the list of valid travelers whenever the user mouses over the combo
    # Makes sure recently added travelers are avaliable to choose.
    traveler_combo.bind("<Enter>", lambda event: update_companion_travelers(event, traveler_combo))
    
    # Button to submit all attributes to controller for insertion.
    submission_button = Button(add_companion_view, text="Add", command=lambda: submit_companion(
        name_string.get(), 
        age_string.get(), 
        location_string.get(), 
        traveler_combo.get()))
    submission_button.grid(row = 4, column = 2, sticky = S, padx = 2, pady = 2)
    return

def build_add_vehicle_frame(add_vehicle_view):
    # Labels for all Vehicle Attributes
    name_label = Label(add_vehicle_view, text="Name:")
    age_lable = Label(add_vehicle_view, text="Power Capacity:")
    location_lable = Label(add_vehicle_view, text="Engine:")
    traveler_lable = Label(add_vehicle_view, text="Piloted By:")
    name_label.grid(row = 0, column = 0, sticky = W, padx = 2, pady = 2)
    age_lable.grid(row = 1, column = 0, sticky = W, padx = 2, pady = 2)
    location_lable.grid(row = 2, column = 0, sticky = W, padx = 2, pady = 2)
    traveler_lable.grid(row = 3, column = 0, sticky = W, padx = 2, pady = 2)

    # Strings and Entry widgets for all Vehicle Attributes
    name_string = StringVar()
    power_string = StringVar()
    engine_string = StringVar()
    valid_travelers = ctrl_obj.select_all("Travelers", False)
    name_entry = Entry(add_vehicle_view, textvariable=name_string)
    power_entry = Entry(add_vehicle_view, textvariable=power_string)
    engine_entry = Entry(add_vehicle_view, textvariable=engine_string)
    traveler_combo = ttk.Combobox(add_vehicle_view, values=valid_travelers, state="readonly")
    name_entry.grid(row = 0, column = 1, pady = 2)
    power_entry.grid(row = 1, column = 1, pady = 2)
    engine_entry.grid(row = 2, column = 1, pady = 2)
    traveler_combo.grid(row = 3, column = 1, pady = 2)

    # Update the list of valid travelers whenever the user mouses over the combo
    # Makes sure recently added travelers are avaliable to choose.
    traveler_combo.bind("<Enter>", lambda event: update_companion_travelers(event, traveler_combo))

    # Button to submit all attributes to controller for insertion.
    submission_button = Button(add_vehicle_view, text="Add", command=lambda: submit_vehicle(
        name_string.get(), 
        power_string.get(), 
        engine_string.get(), 
        traveler_combo.get()))
    submission_button.grid(row = 4, column = 2, sticky = S, padx = 2, pady = 2)
    return

def build_add_tool_frame(add_tool_view):
    # Labels for all Tool Attributes
    name_label = Label(add_tool_view, text="Name:")
    age_lable = Label(add_tool_view, text="Power Capacity:")
    traveler_lable = Label(add_tool_view, text="Utilized By:")
    name_label.grid(row = 0, column = 0, sticky = W, padx = 2, pady = 2)
    age_lable.grid(row = 1, column = 0, sticky = W, padx = 2, pady = 2)
    traveler_lable.grid(row = 2, column = 0, sticky = W, padx = 2, pady = 2)

    # Strings and Entry widgets for all Vehicle Attributes
    name_string = StringVar()
    power_string = StringVar()
    valid_travelers = ctrl_obj.select_all("Travelers", False)
    name_entry = Entry(add_tool_view, textvariable=name_string)
    power_entry = Entry(add_tool_view, textvariable=power_string)
    traveler_combo = ttk.Combobox(add_tool_view, values=valid_travelers, state="readonly")
    name_entry.grid(row = 0, column = 1, pady = 2)
    power_entry.grid(row = 1, column = 1, pady = 2)
    traveler_combo.grid(row = 2, column = 1, pady = 2)

    # Update the list of valid travelers whenever the user mouses over the combo
    # Makes sure recently added travelers are avaliable to choose.
    traveler_combo.bind("<Enter>", lambda event: update_companion_travelers(event, traveler_combo))

    # Button to submit all attributes to controller for insertion.
    submission_button = Button(add_tool_view, text="Add", command=lambda: submit_tool(
        name_string.get(), 
        power_string.get(), 
        traveler_combo.get()))
    submission_button.grid(row = 3, column = 2, sticky = S, padx = 2, pady = 2)
    return

def update_companion_travelers(event, combo):
    # Use config to update the set of acceptable travelers.
    combo.config(values=ctrl_obj.select_all("Travelers", False))
    return

def submit_traveler(name, age, location):
    # Make sure the user wants to insert a companion.
    insert = add_confirmation("Traveler")

    # Break out early if not returning
    if not insert:
        return
    
    # Check user input for errors
    try:
        if name == "" or age == "" or location == "": 
            raise ValueError
    except:
        messagebox.showinfo(message='Error: Entered traveler values are incorrect!')
        return
    
    # if user wants to insert, add the traveler into our db using controller.
    if insert:
        ctrl_obj.insert_traveler(name, age, location)
        messagebox.showinfo(message='Traveler added!')
    return

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
    
def submit_vehicle(name, power_capacity, engine, traveler):
    insert = add_confirmation("Vehicle")

    # Break out early if not returning
    if not insert:
        return
    
    # Check user input for errors
    try:
        temp = traveler[0]
        if name == "" or power_capacity == "" or engine == "": 
            raise ValueError
        # print(name, age, location, traveler[0] if traveler[0] != None else "")
    except IndexError:
        messagebox.showinfo(message='Error: Selected traveler is invalid!')
        return
    except:
        messagebox.showinfo(message='Error: Entered vehicle values are incorrect!')
        return

    # if user wants to insert, add the companion into our db using controller.
    if insert:
        ctrl_obj.insert_vehicle(name, power_capacity, engine, traveler[0])
        messagebox.showinfo(message='Vehicle added!')
        return
    else:
        return

def submit_tool(name, power_capacity, traveler):
    insert = add_confirmation("Tool")

    # Break out early if not returning
    if not insert:
        return
    
    # Check user input for errors
    try:
        temp = traveler[0]
        if name == "" or power_capacity == "": 
            raise ValueError
        # print(name, age, location, traveler[0] if traveler[0] != None else "")
    except IndexError:
        messagebox.showinfo(message='Error: Selected traveler is invalid!')
        return
    except:
        messagebox.showinfo(message='Error: Entered vehicle values are incorrect!')
        return

    # if user wants to insert, add the companion into our db using controller.
    if insert:
        ctrl_obj.insert_tool(name, power_capacity, traveler[0])
        messagebox.showinfo(message='Tool added!')
        return
    else:
        return

def add_confirmation(message):
    return messagebox.askyesno(message=f'Are you sure you want to add this {message}?',
                                 icon='question',
                                 title='Add Confirmation')

def build_database_view(parent):
    global ctrl_obj

    # Notebook containing subviews that we will return
    view_notebook = ttk.Notebook(parent)

    # Frames for viewing entities
    trip_frame = ttk.Frame(view_notebook)
    traveler_frame = ttk.Frame(view_notebook)
    companion_frame = ttk.Frame(view_notebook)
    vehicle_frame = ttk.Frame(view_notebook)
    tool_frame = ttk.Frame(view_notebook)

    # Build frame widgets
    build_view_traveler_frame(traveler_frame)

    # Add frames to notebook
    view_notebook.add(trip_frame, text="Trips")
    view_notebook.add(traveler_frame, text="Travelers")
    view_notebook.add(companion_frame, text="Companions")
    view_notebook.add(vehicle_frame, text="Vehicles")
    view_notebook.add(tool_frame, text="Tools")

    return view_notebook

def build_view_traveler_frame(traveler_frame):
    global ctrl_obj

    # Create the Treeview widget with columns
    traveler_tree = ttk.Treeview(traveler_frame, columns=("id", "Name", "Age", "birthLocation", "time"), show="headings")

    # Define column headings
    traveler_tree.heading("id", text="Traveler ID")
    traveler_tree.heading("Name", text="Name")
    traveler_tree.heading("Age", text="Age")
    traveler_tree.heading("birthLocation", text="Birth Location")
    traveler_tree.heading("time", text="Current Time Period")

    traveler_array = ctrl_obj.select_all("Travelers", True)

    # Populate the Treeview with data from the array
    populate_treeview(traveler_tree, traveler_array)

    traveler_tree.pack(fill="both", expand=True)

    traveler_tree.bind("<Enter>", lambda event: populate_treeview(traveler_tree, ctrl_obj.select_all("Travelers", True)))

    return

def populate_treeview(tree, data):
    # Clear the treeview list items
    for item in tree.get_children():
        tree.delete(item)

    # Insert updated data
    for item in data:
        tree.insert('', 'end', values=item)

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
    add_view = ttk.Frame(root_notebook)   
    edit_view = ttk.Frame(root_notebook)  
    database_view = ttk.Frame(root_notebook)
    export_view = ttk.Frame(root_notebook)

    # Build the subframes for each view, and insert
    add_view_frames = build_add_view(add_view)
    add_view_frames.pack(fill="both", expand=True)
    database_view_frames = build_database_view(database_view)
    database_view_frames.pack(fill="both", expand=True)

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