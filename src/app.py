"""
 * app.py contains the view code to drive the user's view of the database, and 
 * calls the controller in order to execute the user's desired modifications
 * to the database.
"""

# Library imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import pandas as pd

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

    # Build each frame's widgets
    build_add_trip_frame(add_trip_view)
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

def build_add_trip_frame(add_trip_view):
    # Labels for all trip attributes
    location_label = ttk.Label(add_trip_view, text="Location:")
    image_label = ttk.Label(add_trip_view, text="Image File:")
    traveler_lable = ttk.Label(add_trip_view, text="Traveler:")
    location_label.grid(row = 0, column = 0, sticky = W, padx = 4, pady = 2)
    image_label.grid(row = 1, column = 0, sticky = W, padx = 4, pady = 2)
    traveler_lable.grid(row = 2, column = 0, sticky = W, padx = 2, pady = 2)

    # Strings and Entry widgets for all Companion Attributes
    location_string = StringVar()
    image_string = StringVar()
    valid_travelers = ctrl_obj.select_all("Travelers", False)
    location_entry = ttk.Entry(add_trip_view, textvariable=location_string)
    image_entry = ttk.Entry(add_trip_view, textvariable=image_string)
    traveler_combo = ttk.Combobox(add_trip_view, values=valid_travelers, state="readonly")
    location_entry.grid(row = 0, column = 1, pady = 2)
    image_entry.grid(row = 1, column = 1, pady = 2)
    traveler_combo.grid(row = 2, column = 1, pady = 2)

    # Update the list of valid travelers whenever the user mouses over the combo
    # Makes sure recently added travelers are avaliable to choose.
    traveler_combo.bind("<Enter>", lambda event: update_companion_travelers(event, traveler_combo))

    # Button to submit all attributes to controller for insertion.
    submission_button = Button(add_trip_view, text="Add", command=lambda: submit_trip(
        location_string.get(), 
        image_string.get(), 
        traveler_combo.get()))
    submission_button.grid(row = 3, column = 2, sticky = S, padx = 2, pady = 2)

    return

def build_add_traveler_frame(add_traveler_view):
    # Labels for all traveler Attributes
    name_label = ttk.Label(add_traveler_view, text="Name:")
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

def submit_trip(location, image, traveler):
    # Make sure the user wants to insert a trip.
    insert = add_confirmation("Trip")
    
    # Break out early if not returning
    if not insert:
        return
    
    # Check user input for errors
    try:
        temp = traveler[0]
        if location == "" or image == "": 
            raise ValueError
        # print(name, age, location, traveler[0] if traveler[0] != None else "")
    except IndexError:
        messagebox.showinfo(message='Error: Selected traveler is invalid!')
        return
    except:
        messagebox.showinfo(message='Error: Entered trip values are incorrect!')
        return

    # if user wants to insert, add the trip into our db using controller.
    if insert:
        ctrl_obj.insert_trip(location, image, traveler[0])
        messagebox.showinfo(message='Trip added!')
        return
    else:
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

def build_edit_view(parent):
    global ctrl_obj

    # Notebook containing subviews for selecting & editing from tables
    edit_root_notebook = ttk.Notebook(parent)

    # Build each notebook
    # Frames for containing widgets for accessing, editing, and deleting.
    edit_trip_frame = ttk.Frame(edit_root_notebook)
    edit_traveler_frame = ttk.Frame(edit_root_notebook)
    edit_companion_frame = ttk.Frame(edit_root_notebook)
    edit_tool_frame = ttk.Frame(edit_root_notebook)
    edit_vehicle_frame = ttk.Frame(edit_root_notebook)
    edit_tool_ability_frame = ttk.Frame(edit_root_notebook)
    edit_vehicle_ability_frame = ttk.Frame(edit_root_notebook)

    # Build frame widgets
    build_edit_trip_frame(edit_trip_frame)

    # Add frames to notebook
    edit_root_notebook.add(edit_trip_frame, text="Trip")

    return edit_root_notebook

def build_edit_trip_frame(edit_trip_frame):
    global ctrl_obj

    # Create the Treeview widget with columns
    trip_tree = ttk.Treeview(edit_trip_frame, columns=("id", "location", "date", "image", "ttid"), show="headings")

    # Define column headings
    trip_tree.heading("id", text="Trip ID")
    trip_tree.heading("location", text="Location")
    trip_tree.heading("date", text="Date")
    trip_tree.heading("image", text="Image File")
    trip_tree.heading("ttid", text="Traveler ID")

    # Get data from database to display
    trip_array = ctrl_obj.select_all("Trips", True)

    # Populate the Treeview with data from the array
    populate_treeview(trip_tree, trip_array)

    # Arrange the tree within the frame
    trip_tree.pack(fill="both", expand=True)

    # Dynamically update on cursor hover
    trip_tree.bind("<Enter>", lambda event: populate_treeview(trip_tree, ctrl_obj.select_all("Trips", True)))

    # Edit and Delete buttons
    delete_button = ttk.Button(edit_trip_frame, text='Delete Item', command=lambda: drop_item(trip_tree, "Trip"))
    delete_button.pack(side="left")

    select_button = ttk.Button(edit_trip_frame, text='Edit Item', command=lambda: edit_item(trip_tree, "Trip"))
    select_button.pack(side="right")

def edit_item(tree, table):
    global ctrl_obj

    target_tuple = get_tree_row(tree)
    primary_key = target_tuple[0]

    if primary_key == None:
        return
    
    print(primary_key)

def drop_item(tree, table):
    global ctrl_obj

    primary_key = get_tree_row(tree)
    primary_key = primary_key[0]

    if primary_key == None:
        return
    
    ctrl_obj.drop_tuple(primary_key, table)

def get_tree_row(tree):
    selected_item = tree.selection()
    if selected_item:
        # print("Selected item:", selected_item[0])
        values = tree.item(selected_item[0], 'values')
        # print("Values:", values)
        return values
    else:
        # print("No item selected")
        return None

def build_database_view(parent):
    global ctrl_obj

    # Notebook containing subviews that we will return
    view_notebook = ttk.Notebook(parent)
    table_notebook = ttk.Notebook(view_notebook)
    aggregate_notebook = ttk.Notebook(view_notebook)

    # Build the view notebook.
    # Frames for viewing entities
    trip_frame = ttk.Frame(table_notebook)
    traveler_frame = ttk.Frame(table_notebook)
    companion_frame = ttk.Frame(table_notebook)
    vehicle_frame = ttk.Frame(table_notebook)
    tool_frame = ttk.Frame(table_notebook)

    # Build frame widgets
    build_view_trip_frame(trip_frame)
    build_view_traveler_frame(traveler_frame)
    build_view_companion_frame(companion_frame)
    build_view_vehicle_frame(vehicle_frame)
    build_view_tool_frame(tool_frame)

    # Add frames to notebook
    table_notebook.add(trip_frame, text="Trips")
    table_notebook.add(traveler_frame, text="Travelers")
    table_notebook.add(companion_frame, text="Companions")
    table_notebook.add(vehicle_frame, text="Vehicles")
    table_notebook.add(tool_frame, text="Tools")

    # Build the aggregation notebook
    # The frame
    aggregation_frame = ttk.Frame(aggregate_notebook)
    aggregation_frame.pack(fill="both", expand=True)

    # Populate the frame
    build_view_aggregation_frame(aggregation_frame)

    # Add all types of notebooks to the parent notebook.
    view_notebook.add(table_notebook, text="Table Views")
    view_notebook.add(aggregate_notebook, text="Aggregation Views")

    return view_notebook

def build_view_trip_frame(trip_frame):
    global ctrl_obj

    # Create the Treeview widget with columns
    trip_tree = ttk.Treeview(trip_frame, columns=("id", "location", "date", "image", "ttid"), show="headings")

    # Define column headings
    trip_tree.heading("id", text="Trip ID")
    trip_tree.heading("location", text="Location")
    trip_tree.heading("date", text="Date")
    trip_tree.heading("image", text="Image File")
    trip_tree.heading("ttid", text="Traveler ID")

    # Get data from database to display
    trip_array = ctrl_obj.select_all("Trips", True)

    # Populate the Treeview with data from the array
    populate_treeview(trip_tree, trip_array)

    # Arrange the tree within the frame
    trip_tree.pack(fill="both", expand=True)

    # Dynamically update on cursor hover
    trip_tree.bind("<Enter>", lambda event: populate_treeview(trip_tree, ctrl_obj.select_all("Trips", True)))
    return

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

    # Get data from database to display
    traveler_array = ctrl_obj.select_all("Travelers", True)

    # Populate the Treeview with data from the array
    populate_treeview(traveler_tree, traveler_array)

    # Arrange the tree within the frame
    traveler_tree.pack(fill="both", expand=True)

    # Dynamically update on cursor hover
    traveler_tree.bind("<Enter>", lambda event: populate_treeview(traveler_tree, ctrl_obj.select_all("Travelers", True)))
    return

def build_view_companion_frame(companion_frame):
    global ctrl_obj

    # Create the Treeview widget with columns
    companion_tree = ttk.Treeview(companion_frame, columns=("id", "Name", "Age", "originalLocation", "time", "ttid"), show="headings")

    # Define column headings
    companion_tree.heading("id", text="Companion ID")
    companion_tree.heading("Name", text="Name")
    companion_tree.heading("Age", text="Age")
    companion_tree.heading("originalLocation", text="Original Location")
    companion_tree.heading("time", text="Current Time Period")
    companion_tree.heading("ttid", text="Traveler ID")

    # Get data from database to display
    companion_array = ctrl_obj.select_all("Companions", True)

    # Populate the Treeview with data from the array
    populate_treeview(companion_tree, companion_array)

    # Arrange the tree within the frame
    companion_tree.pack(fill="both", expand=True)

    # Dynamically update on cursor hover
    companion_tree.bind("<Enter>", lambda event: populate_treeview(companion_tree, ctrl_obj.select_all("Companions", True)))
    return

def build_view_vehicle_frame(vehicle_frame):
    global ctrl_obj

    # Create the Treeview widget with columns
    vehicle_tree = ttk.Treeview(vehicle_frame, columns=("id", "name", "capacity", "engine", "ttid"), show="headings")

    # Define column headings
    vehicle_tree.heading("id", text="Vehicle ID")
    vehicle_tree.heading("name", text="Name")
    vehicle_tree.heading("capacity", text="Power Capacity")
    vehicle_tree.heading("engine", text="Engine")
    vehicle_tree.heading("ttid", text="Traveler ID")

    # Get data from database to display
    vehicle_array = ctrl_obj.select_all("Vehicles", True)

    # Populate the Treeview with data from the array
    populate_treeview(vehicle_tree, vehicle_array)

    # Arrange the tree within the frame
    vehicle_tree.pack(fill="both", expand=True)

    # Dynamically update on cursor hover
    vehicle_tree.bind("<Enter>", lambda event: populate_treeview(vehicle_tree, ctrl_obj.select_all("Vehicles", True)))
    return

def build_view_tool_frame(tool_frame):
    global ctrl_obj

    # Create the Treeview widget with columns
    tool_tree = ttk.Treeview(tool_frame, columns=("id", "name", "capacity", "ttid"), show="headings")

    # Define column headings
    tool_tree.heading("id", text="Tool ID")
    tool_tree.heading("name", text="Name")
    tool_tree.heading("capacity", text="Power Capacity")
    tool_tree.heading("ttid", text="Traveler ID")

    # Get data from database to display
    tool_array = ctrl_obj.select_all("Tools", True)

    # Populate the Treeview with data from the array
    populate_treeview(tool_tree, tool_array)

    # Arrange the tree within the frame
    tool_tree.pack(fill="both", expand=True)

    # Dynamically update on cursor hover
    tool_tree.bind("<Enter>", lambda event: populate_treeview(tool_tree, ctrl_obj.select_all("Tools", True)))
    return

def populate_treeview(tree, data):
    # Clear the treeview list items
    for item in tree.get_children():
        tree.delete(item)

    # Insert updated data
    for item in data:
        tree.insert('', 'end', values=item)

def build_view_aggregation_frame(aggregation_frame):
    global ctrl_obj

    # Data from Database
    total_travlers = ctrl_obj.get_count("Traveler", "*")
    total_companions = ctrl_obj.get_count("Companion", "*")
    total_trips = ctrl_obj.get_count("Trip", "*")
    total_tools = ctrl_obj.get_count("Tool", "*")
    total_vehicles = ctrl_obj.get_count("Vehicle", "*")
    average_trips_per_traveler = ctrl_obj.get_average_trips("travelerID")
    average_trips_per_companion = ctrl_obj.get_average_trips("companionID")
    average_tool_power = ctrl_obj.get_average("Tool", "powerCapacity", None)
    average_vehicle_power = ctrl_obj.get_average("Vehicle", "powerCapacity", None)

    # Label Objects
    total_travelers_label = ttk.Label(aggregation_frame, text="Total Travelers:")
    total_companions_label = ttk.Label(aggregation_frame, text="Total Companions:")
    total_trips_label = ttk.Label(aggregation_frame, text="Total Trips:")
    total_tools_label = ttk.Label(aggregation_frame, text="Total Tools:")
    total_vehicles_label = ttk.Label(aggregation_frame, text="Total Vehicles:")
    average_trips_traveler_label = ttk.Label(aggregation_frame, text="Average Trips per Traveler:")
    average_trips_companion_label = ttk.Label(aggregation_frame, text="Average Trips per Companion:")
    average_tool_power_label = ttk.Label(aggregation_frame, text="Average Tool Power:")
    average_vehicle_power_label = ttk.Label(aggregation_frame, text="Average Vehicle Power:")

    total_travelers_amt = ttk.Label(aggregation_frame, text=total_travlers)
    total_companions_amt = ttk.Label(aggregation_frame, text=total_companions)
    total_trip_amt = ttk.Label(aggregation_frame, text=total_trips)
    total_tool_amt = ttk.Label(aggregation_frame, text=total_tools)
    total_vehicle_amt = ttk.Label(aggregation_frame, text=total_vehicles)
    trip_traveler_avg = ttk.Label(aggregation_frame, text=average_trips_per_traveler)
    trip_companion_avg = ttk.Label(aggregation_frame, text=average_trips_per_companion)
    tool_power_avg = ttk.Label(aggregation_frame, text=average_tool_power)
    vehicle_power_avg = ttk.Label(aggregation_frame, text=average_vehicle_power)

    # Arrage Labels
    total_travelers_label.grid(row = 0, column=0, pady = 0, sticky="E")
    total_companions_label.grid(row = 1, column=0, pady = 0, sticky="E")
    total_trips_label.grid(row = 2, column=0, pady = 0, sticky="E")
    total_tools_label.grid(row = 3, column=0, pady = 0, sticky="E")
    total_vehicles_label.grid(row = 4, column=0, pady = 0, sticky="E")
    average_trips_traveler_label.grid(row = 5, column=0, pady = 0, sticky="E")
    average_trips_companion_label.grid(row = 6, column=0, pady = 0, sticky="E")
    average_tool_power_label.grid(row = 7, column=0, pady = 0, sticky="E")
    average_vehicle_power_label.grid(row = 8, column=0, pady = 0, sticky="E")

    total_travelers_amt.grid(row = 0, column = 1, pady = 0, sticky="W")
    total_companions_amt.grid(row = 1, column = 1, pady = 0, sticky="W")
    total_trip_amt.grid(row = 2, column = 1, pady = 0, sticky="W")
    total_tool_amt.grid(row = 3, column = 1, pady = 0, sticky="W")
    total_vehicle_amt.grid(row = 4, column = 1, pady = 0, sticky="W")
    trip_traveler_avg.grid(row = 5, column = 1, pady = 0, sticky="W")
    trip_companion_avg.grid(row = 6, column = 1, pady = 0, sticky="W")
    tool_power_avg.grid(row = 7, column = 1, pady = 0, sticky="W")
    vehicle_power_avg.grid(row = 8, column = 1, pady = 0, sticky="W")

    return

def build_export_view(parent):
    global ctrl_obj

    # Base Frame Object
    export_frame = ttk.Frame(parent)

    # Label Widgets
    export_header = ttk.Label(export_frame, text="Time Traveler's Database Report:")

    # Frame all items
    export_header.grid(row = 0, column = 0, pady = 2)

    # Button to send request to download Excel sheet..
    submission_button = Button(export_frame, text="Generate Database Report", command=lambda: generate_database_report())
    submission_button.grid(row = 0, column = 2, sticky = S, padx = 2, pady = 2)

    return export_frame

def generate_database_report():
    global ctrl_obj

    # Ask if user wants to save a report.
    generate_confirmation = export_confirmation()

    if generate_confirmation:
        # If they do, get components needed for a report from the DB.
        report_array = ctrl_obj.generate_report()
        columns = ctrl_obj.get_column_names("v_master_records")

        # Ask the user where they want to save their report to.
        file_path = filedialog.asksaveasfile(mode='w', defaultextension=".csv")
        
        # If user bails on saving, abort serializing the repot.
        if file_path is None:
            return

        # Write the report to the intended file path.
        report_df = pd.DataFrame(report_array, columns=columns)
        report_df.to_csv(file_path.name, index=False)
        file_path.close()

    return

def export_confirmation():
    return messagebox.askyesno(message=f'Are you sure you want to generate a report of the database?',
                                 icon='question',
                                 title='Generate Report?')

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
    edit_view_frames = build_edit_view(edit_view)
    database_view_frames = build_database_view(database_view)
    export_view_frames = build_export_view(export_view)
    add_view_frames.pack(fill="both", expand=True)
    edit_view_frames.pack(fill="both", expand=True)
    database_view_frames.pack(fill="both", expand=True)
    export_view_frames.pack(fill="both", expand=True)

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