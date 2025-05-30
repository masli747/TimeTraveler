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

from ttkthemes import *

# Local DB imports
from controller import controller
from constants import Constants
# from src.constants import Constants


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
    submission_button = ttk.Button(add_trip_view, text="Add", command=lambda: submit_trip(
        location_string.get(),
        image_string.get(),
        traveler_combo.get()))
    submission_button.grid(row = 3, column = 2, sticky = S, padx = 2, pady = 2)

    return

def build_add_traveler_frame(add_traveler_view):
    # Labels for all traveler Attributes
    name_label = ttk.Label(add_traveler_view, text="Name:")
    age_lable = ttk.Label(add_traveler_view, text="Age:")
    location_lable = ttk.Label(add_traveler_view, text="Original Location:")
    name_label.grid(row = 0, column = 0, sticky = W, padx = 4, pady = 2)
    age_lable.grid(row = 1, column = 0, sticky = W, padx = 4, pady = 2)
    location_lable.grid(row = 2, column = 0, sticky = W, padx = 4, pady = 2)

    # Strings and ttk.Entry widgets for all Companion Attributes
    name_string = StringVar()
    age_string = StringVar()
    location_string = StringVar()
    name_entry = ttk.Entry(add_traveler_view, textvariable=name_string)
    age_entry = ttk.Entry(add_traveler_view, textvariable=age_string)
    location_entry = ttk.Entry(add_traveler_view, textvariable=location_string)
    name_entry.grid(row = 0, column = 1, pady = 2)
    age_entry.grid(row = 1, column = 1, pady = 2)
    location_entry.grid(row = 2, column = 1, pady = 2)

    # ttk.Button to submit all attributes to controller for insertion.
    submission_button = ttk.Button(add_traveler_view, text="Add", command=lambda: submit_traveler(
        name_string.get(), 
        age_string.get(), 
        location_string.get()))
    submission_button.grid(row = 3, column = 2, sticky = S, padx = 2, pady = 2)

    return

def build_add_companion_frame(add_companion_view):
    # ttk.Labels for all Companion Attributes
    name_label = ttk.Label(add_companion_view, text="Name:")
    age_lable = ttk.Label(add_companion_view, text="Age:")
    location_lable = ttk.Label(add_companion_view, text="Original Location:")
    traveler_lable = ttk.Label(add_companion_view, text="Travels With:")
    name_label.grid(row = 0, column = 0, sticky = W, padx = 2, pady = 2)
    age_lable.grid(row = 1, column = 0, sticky = W, padx = 2, pady = 2)
    location_lable.grid(row = 2, column = 0, sticky = W, padx = 2, pady = 2)
    traveler_lable.grid(row = 3, column = 0, sticky = W, padx = 2, pady = 2)
    
    # Strings and ttk.Entry widgets for all Companion Attributes
    name_string = StringVar()
    age_string = StringVar()
    location_string = StringVar()
    valid_travelers = ctrl_obj.select_all("Travelers", False)
    name_entry = ttk.Entry(add_companion_view, textvariable=name_string)
    age_entry = ttk.Entry(add_companion_view, textvariable=age_string)
    location_entry = ttk.Entry(add_companion_view, textvariable=location_string)
    traveler_combo = ttk.Combobox(add_companion_view, values=valid_travelers, state="readonly")
    name_entry.grid(row = 0, column = 1, pady = 2)
    age_entry.grid(row = 1, column = 1, pady = 2)
    location_entry.grid(row = 2, column = 1, pady = 2)
    traveler_combo.grid(row = 3, column = 1, pady = 2)

    # Update the list of valid travelers whenever the user mouses over the combo
    # Makes sure recently added travelers are avaliable to choose.
    traveler_combo.bind("<Enter>", lambda event: update_companion_travelers(event, traveler_combo))
    
    # ttk.Button to submit all attributes to controller for insertion.
    submission_button = ttk.Button(add_companion_view, text="Add", command=lambda: submit_companion(
        name_string.get(), 
        age_string.get(), 
        location_string.get(), 
        traveler_combo.get()))
    submission_button.grid(row = 4, column = 2, sticky = S, padx = 2, pady = 2)
    return

def build_add_vehicle_frame(add_vehicle_view):
    # ttk.Labels for all Vehicle Attributes
    name_label = ttk.Label(add_vehicle_view, text="Name:")
    age_lable = ttk.Label(add_vehicle_view, text="Power Capacity:")
    location_lable = ttk.Label(add_vehicle_view, text="Engine:")
    traveler_lable = ttk.Label(add_vehicle_view, text="Piloted By:")
    name_label.grid(row = 0, column = 0, sticky = W, padx = 2, pady = 2)
    age_lable.grid(row = 1, column = 0, sticky = W, padx = 2, pady = 2)
    location_lable.grid(row = 2, column = 0, sticky = W, padx = 2, pady = 2)
    traveler_lable.grid(row = 3, column = 0, sticky = W, padx = 2, pady = 2)

    # Strings and ttk.Entry widgets for all Vehicle Attributes
    name_string = StringVar()
    power_string = StringVar()
    engine_string = StringVar()
    valid_travelers = ctrl_obj.select_all("Travelers", False)
    name_entry = ttk.Entry(add_vehicle_view, textvariable=name_string)
    power_entry = ttk.Entry(add_vehicle_view, textvariable=power_string)
    engine_entry = ttk.Entry(add_vehicle_view, textvariable=engine_string)
    traveler_combo = ttk.Combobox(add_vehicle_view, values=valid_travelers, state="readonly")
    name_entry.grid(row = 0, column = 1, pady = 2)
    power_entry.grid(row = 1, column = 1, pady = 2)
    engine_entry.grid(row = 2, column = 1, pady = 2)
    traveler_combo.grid(row = 3, column = 1, pady = 2)

    # Update the list of valid travelers whenever the user mouses over the combo
    # Makes sure recently added travelers are avaliable to choose.
    traveler_combo.bind("<Enter>", lambda event: update_companion_travelers(event, traveler_combo))

    # ttk.Button to submit all attributes to controller for insertion.
    submission_button = ttk.Button(add_vehicle_view, text="Add", command=lambda: submit_vehicle(
        name_string.get(), 
        power_string.get(), 
        engine_string.get(), 
        traveler_combo.get()))
    submission_button.grid(row = 4, column = 2, sticky = S, padx = 2, pady = 2)
    return

def build_add_tool_frame(add_tool_view):
    # ttk.Labels for all Tool Attributes
    name_label = ttk.Label(add_tool_view, text="Name:")
    age_lable = ttk.Label(add_tool_view, text="Power Capacity:")
    traveler_lable = ttk.Label(add_tool_view, text="Utilized By:")
    name_label.grid(row = 0, column = 0, sticky = W, padx = 2, pady = 2)
    age_lable.grid(row = 1, column = 0, sticky = W, padx = 2, pady = 2)
    traveler_lable.grid(row = 2, column = 0, sticky = W, padx = 2, pady = 2)

    # Strings and ttk.Entry widgets for all Vehicle Attributes
    name_string = StringVar()
    power_string = StringVar()
    valid_travelers = ctrl_obj.select_all("Travelers", False)
    name_entry = ttk.Entry(add_tool_view, textvariable=name_string)
    power_entry = ttk.Entry(add_tool_view, textvariable=power_string)
    traveler_combo = ttk.Combobox(add_tool_view, values=valid_travelers, state="readonly")
    name_entry.grid(row = 0, column = 1, pady = 2)
    power_entry.grid(row = 1, column = 1, pady = 2)
    traveler_combo.grid(row = 2, column = 1, pady = 2)

    # Update the list of valid travelers whenever the user mouses over the combo
    # Makes sure recently added travelers are avaliable to choose.
    traveler_combo.bind("<Enter>", lambda event: update_companion_travelers(event, traveler_combo))

    # ttk.Button to submit all attributes to controller for insertion.
    submission_button = ttk.Button(add_tool_view, text="Add", command=lambda: submit_tool(
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

def update_confirmation():
    return messagebox.askyesno(message=f'Are you sure you want to update this entry?',
                                 icon='question',
                                 title='Entry Confirmation')

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
    build_edit_traveler_frame(edit_traveler_frame)
    build_edit_companion_frame(edit_companion_frame)
    build_edit_vehicle_frame(edit_vehicle_frame)
    build_edit_tool_frame(edit_tool_frame)

    # Add frames to notebook
    edit_root_notebook.add(edit_trip_frame, text="Trip")
    edit_root_notebook.add(edit_traveler_frame, text="Traveler")
    edit_root_notebook.add(edit_companion_frame, text="Companion")
    edit_root_notebook.add(edit_vehicle_frame, text="Vehicle")
    edit_root_notebook.add(edit_tool_frame, text="Tool")

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

    edit_button = ttk.Button(edit_trip_frame, text='Edit Item', command=lambda: edit_item(trip_tree, "Trip", edit_trip_frame))
    edit_button.pack(side="right")

def build_edit_traveler_frame(edit_trip_frame):
    global ctrl_obj

   # Create the Treeview widget with columns
    traveler_tree = ttk.Treeview(edit_trip_frame, columns=("id", "Name", "Age", "birthLocation", "time"), show="headings")

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

    # Edit and Delete buttons
    delete_button = ttk.Button(edit_trip_frame, text='Delete Item', command=lambda: drop_item(traveler_tree, "Traveler"))
    delete_button.pack(side="left")

    edit_button = ttk.Button(edit_trip_frame, text='Edit Item', command=lambda: edit_item(traveler_tree, "Traveler", edit_trip_frame))
    edit_button.pack(side="right")

def build_edit_companion_frame(edit_companion_frame):
    global ctrl_obj

    # Create the Treeview widget with columns
    companion_tree = ttk.Treeview(edit_companion_frame, columns=("id", "Name", "Age", "originalLocation", "time", "ttid"), show="headings")

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

    # Edit and Delete buttons
    delete_button = ttk.Button(edit_companion_frame, text='Delete Item', command=lambda: drop_item(companion_tree, "Companion"))
    delete_button.pack(side="left")

    edit_button = ttk.Button(edit_companion_frame, text='Edit Item', command=lambda: edit_item(companion_tree, "Companion", edit_companion_frame))
    edit_button.pack(side="right")

def build_edit_vehicle_frame(edit_vehicle_frame):
    global ctrl_obj

    # Create the Treeview widget with columns
    vehicle_tree = ttk.Treeview(edit_vehicle_frame, columns=("id", "name", "capacity", "engine", "ttid"), show="headings")

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

    # Edit and Delete buttons
    delete_button = ttk.Button(edit_vehicle_frame, text='Delete Item', command=lambda: drop_item(vehicle_tree, "Vehicle"))
    delete_button.pack(side="left")

    edit_button = ttk.Button(edit_vehicle_frame, text='Edit Item', command=lambda: edit_item(vehicle_tree, "Vehicle", edit_vehicle_frame))
    edit_button.pack(side="right")

def build_edit_tool_frame(edit_tool_frame):
    global ctrl_obj

    # Create the Treeview widget with columns
    tool_tree = ttk.Treeview(edit_tool_frame, columns=("id", "name", "capacity", "ttid"), show="headings")

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

    # Edit and Delete buttons
    delete_button = ttk.Button(edit_tool_frame, text='Delete Item', command=lambda: drop_item(tool_tree, "Tool"))
    delete_button.pack(side="left")

    edit_button = ttk.Button(edit_tool_frame, text='Edit Item', command=lambda: edit_item(tool_tree, "Tool", edit_tool_frame))
    edit_button.pack(side="right")

def edit_trip_window(tuple, table, parent):
    trip_window = Toplevel(parent)
    trip_window.title("Edit Trip")
    trip_window.geometry("800x600")

    location_string = StringVar()
    location_string.set(tuple[1])
    image_string = StringVar()
    image_string.set(tuple[3])
    valid_travelers = ctrl_obj.select_all("Travelers", False)

    Label(trip_window, text="Location:").grid(row = 0, column = 0, sticky = E, padx = 2, pady = 2)
    Label(trip_window, text="Image File:").grid(row = 1, column = 0, sticky = E, padx = 2, pady = 2)
    Label(trip_window, text="Traveler ID:").grid(row = 2, column = 0, sticky = E, padx = 2, pady = 2)

    Entry(trip_window, textvariable=location_string).grid(row = 0, column = 1, sticky = W, padx = 2, pady = 2)
    Entry(trip_window, textvariable=image_string).grid(row = 1, column = 1, sticky = W, padx = 2, pady = 2)
    traveler_combo = ttk.Combobox(trip_window, values=valid_travelers, state="readonly")
    traveler_combo.grid(row = 2, column = 1, sticky = W, padx = 2, pady = 2)

    # Update the list of valid travelers whenever the user mouses over the combo
    # Makes sure recently added travelers are avaliable to choose.
    traveler_combo.bind("<Enter>", lambda event: update_companion_travelers(event, traveler_combo))

    # Button to submit all attributes to controller for update.
    submission_button = Button(trip_window, text="Update", command=lambda: update_tuple(
        "Trip",
        (
            tuple[0],
            f"\'{location_string.get()}\'",
            f"\'{image_string.get()}\'",
            traveler_combo.get()[0])))
    submission_button.grid(row = 3, column = 2, sticky = S, padx = 2, pady = 2)

def edit_traveler_window(tuple, table, parent):
    traveler_window = Toplevel(parent)
    traveler_window.title("Edit Trip")
    traveler_window.geometry("800x600")

    name_string = StringVar()
    name_string.set(tuple[1])
    age_string = StringVar()
    age_string.set(tuple[2])
    birthplace_string = StringVar()
    birthplace_string.set(tuple[3])

    Label(traveler_window, text="Name:").grid(row = 0, column = 0, sticky = E, padx = 2, pady = 2)
    Label(traveler_window, text="Age:").grid(row = 1, column = 0, sticky = E, padx = 2, pady = 2)
    Label(traveler_window, text="Birth Location:").grid(row = 2, column = 0, sticky = E, padx = 2, pady = 2)

    Entry(traveler_window, textvariable=name_string).grid(row = 0, column = 1, sticky = W, padx = 2, pady = 2)
    Entry(traveler_window, textvariable=age_string).grid(row = 1, column = 1, sticky = W, padx = 2, pady = 2)
    Entry(traveler_window, textvariable=birthplace_string).grid(row = 2, column = 1, sticky = W, padx = 2, pady = 2)

    # Button to submit all attributes to controller for update.
    submission_button = Button(traveler_window, text="Update", command=lambda: update_tuple(
        "Traveler",
        (
            tuple[0],
            f"\'{name_string.get()}\'",
            age_string.get(),
            f"\'{birthplace_string.get()}\'",
            f"\'{tuple[4]}\'")))
    submission_button.grid(row = 3, column = 2, sticky = S, padx = 2, pady = 2)

def edit_companion_window(tuple, table, parent):
    companion_window = Toplevel(parent)
    companion_window.title("Edit Companion")
    companion_window.geometry("800x600")

    name_string = StringVar()
    name_string.set(tuple[1])
    age_string = StringVar()
    age_string.set(tuple[2])
    origin_string = StringVar()
    origin_string.set(tuple[3])
    valid_travelers = ctrl_obj.select_all("Travelers", False)

    Label(companion_window, text="Name:").grid(row = 0, column = 0, sticky = E, padx = 2, pady = 2)
    Label(companion_window, text="Age:").grid(row = 1, column = 0, sticky = E, padx = 2, pady = 2)
    Label(companion_window, text="Original Location:").grid(row = 2, column = 0, sticky = E, padx = 2, pady = 2)
    Label(companion_window, text="travelerID:").grid(row = 3, column = 0, sticky = E, padx = 2, pady = 2)

    Entry(companion_window, textvariable=name_string).grid(row = 0, column = 1, sticky = W, padx = 2, pady = 2)
    Entry(companion_window, textvariable=age_string).grid(row = 1, column = 1, sticky = W, padx = 2, pady = 2)
    Entry(companion_window, textvariable=origin_string).grid(row = 2, column = 1, sticky = W, padx = 2, pady = 2)
    traveler_combo = ttk.Combobox(companion_window, values=valid_travelers, state="readonly")
    traveler_combo.grid(row = 3, column = 1, sticky = W, padx = 3, pady = 2)

    # Update the list of valid travelers whenever the user mouses over the combo
    # Makes sure recently added travelers are avaliable to choose.
    traveler_combo.bind("<Enter>", lambda event: update_companion_travelers(event, traveler_combo))

    # Button to submit all attributes to controller for update.
    submission_button = Button(companion_window, text="Update", command=lambda: update_tuple(
        "Companion",
        (
            tuple[0],
            f"\'{name_string.get()}\'",
            age_string.get(),
            f"\'{origin_string.get()}\'",
            f"\'{tuple[4]}\'",
            traveler_combo.get()[0])))
    submission_button.grid(row = 4, column = 2, sticky = S, padx = 2, pady = 2)

def edit_vehicle_window(tuple, table, parent):
    vehicle_window = Toplevel(parent)
    vehicle_window.title("Edit Vehicle")
    vehicle_window.geometry("800x600")

    name_string = StringVar()
    name_string.set(tuple[1])
    power_capacity_string = StringVar()
    power_capacity_string.set(tuple[2])
    engine_string = StringVar()
    engine_string.set(tuple[3])
    valid_travelers = ctrl_obj.select_all("Travelers", False)

    Label(vehicle_window, text="Name:").grid(row = 0, column = 0, sticky = E, padx = 2, pady = 2)
    Label(vehicle_window, text="Power Capacity:").grid(row = 1, column = 0, sticky = E, padx = 2, pady = 2)
    Label(vehicle_window, text="Engine:").grid(row = 2, column = 0, sticky = E, padx = 2, pady = 2)
    Label(vehicle_window, text="travelerID:").grid(row = 3, column = 0, sticky = E, padx = 2, pady = 2)

    Entry(vehicle_window, textvariable=name_string).grid(row = 0, column = 1, sticky = W, padx = 2, pady = 2)
    Entry(vehicle_window, textvariable=power_capacity_string).grid(row = 1, column = 1, sticky = W, padx = 2, pady = 2)
    Entry(vehicle_window, textvariable=engine_string).grid(row = 2, column = 1, sticky = W, padx = 2, pady = 2)
    traveler_combo = ttk.Combobox(vehicle_window, values=valid_travelers, state="readonly")
    traveler_combo.grid(row = 3, column = 1, sticky = W, padx = 3, pady = 2)
    # Update the list of valid travelers whenever the user mouses over the combo
    # Makes sure recently added travelers are avaliable to choose.
    traveler_combo.bind("<Enter>", lambda event: update_companion_travelers(event, traveler_combo))

    # Button to submit all attributes to controller for update.
    submission_button = Button(vehicle_window, text="Update", command=lambda: update_tuple(
        "Vehicle",
        (
            tuple[0],
            f"\'{name_string.get()}\'",
            power_capacity_string.get(),
            f"\'{engine_string.get()}\'",
            traveler_combo.get()[0])))
    submission_button.grid(row = 4, column = 2, sticky = S, padx = 2, pady = 2)

def edit_tool_window(tuple, table, parent):
    tool_window = Toplevel(parent)
    tool_window.title("Edit Tool")
    tool_window.geometry("800x600")

    name_string = StringVar()
    name_string.set(tuple[1])
    power_capacity_string = StringVar()
    power_capacity_string.set(tuple[2])
    valid_travelers = ctrl_obj.select_all("Travelers", False)

    Label(tool_window, text="Name:").grid(row = 0, column = 0, sticky = E, padx = 2, pady = 2)
    Label(tool_window, text="Power Capacity:").grid(row = 1, column = 0, sticky = E, padx = 2, pady = 2)
    Label(tool_window, text="travelerID:").grid(row = 2, column = 0, sticky = E, padx = 2, pady = 2)

    Entry(tool_window, textvariable=name_string).grid(row = 0, column = 1, sticky = W, padx = 2, pady = 2)
    Entry(tool_window, textvariable=power_capacity_string).grid(row = 1, column = 1, sticky = W, padx = 2, pady = 2)
    traveler_combo = ttk.Combobox(tool_window, values=valid_travelers, state="readonly")
    traveler_combo.grid(row = 2, column = 1, sticky = W, padx = 3, pady = 2)
    # Update the list of valid travelers whenever the user mouses over the combo
    # Makes sure recently added travelers are avaliable to choose.
    traveler_combo.bind("<Enter>", lambda event: update_companion_travelers(event, traveler_combo))

    # Button to submit all attributes to controller for update.
    submission_button = Button(tool_window, text="Update", command=lambda: update_tuple(
        "Tool",
        (
            tuple[0],
            f"\'{name_string.get()}\'",
            power_capacity_string.get(),
            traveler_combo.get()[0])))
    submission_button.grid(row = 3, column = 2, sticky = S, padx = 2, pady = 2)

def update_tuple(table, tuple):
    print(tuple) # FIXME: DELETE ME!!!

    # Make sure the user wants to insert a trip.
    insert = update_confirmation()

    # Break out early if not returning
    if not insert:
        return

    ctrl_obj.update_tuple(table, tuple)
    # if user wants to insert, add the trip into our db using controller.
    if insert:
        try:
            # ctrl_obj.update_tuple(table, tuple)
            messagebox.showinfo(message='Entry Updated!')
            return
        except:
            messagebox.showinfo(message='Error: Inputs Invalid!')
            return
    else:
        return
    return

def edit_item(tree, table, parent):
    global ctrl_obj

    target_tuple = get_tree_row(tree)

    if target_tuple == None:
        return

    if table == "Trip":
        edit_trip_window(target_tuple, table, parent)
    elif table == "Traveler":
        edit_traveler_window(target_tuple, table, parent)
    elif table == "Companion":
        edit_companion_window(target_tuple, table, parent)
    elif table == "Vehicle":
        edit_vehicle_window(target_tuple, table, parent)
    elif table == "Tool":
        edit_tool_window(target_tuple, table, parent)
    elif table == "VehicleAbility":
        target_key = "vehicleAbilityID"
    elif table == "ToolAbility":
        target_key = "toolAbilityID"
    else:
        return

def drop_item(tree, table):
    global ctrl_obj

    primary_key = get_tree_row(tree)

    if primary_key == None:
        return

    primary_key = primary_key[0]

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

    # Dynamically update on cursor hover
    aggregation_frame.bind("<Enter>", lambda event: force_aggregate_redraw(aggregation_frame))

    # Add all types of notebooks to the parent notebook.
    view_notebook.add(table_notebook, text="Table Views")
    view_notebook.add(aggregate_notebook, text="Aggregation Views")

    return view_notebook

def force_aggregate_redraw(aggregate_frame):
    for widget in aggregate_frame.winfo_children():
        widget.destroy()

    build_view_aggregation_frame(aggregate_frame)
    return

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
    average_tool_power_after_trip = ctrl_obj.get_average_power_after_trip("Tool")
    average_vehicle_power = ctrl_obj.get_average("Vehicle", "powerCapacity", None)
    average_vehicle_power_after_trip = ctrl_obj.get_average_power_after_trip("Vehicle")

    # Label Objects
    total_travelers_label = ttk.Label(aggregation_frame, text="Total Travelers:")
    total_companions_label = ttk.Label(aggregation_frame, text="Total Companions:")
    total_trips_label = ttk.Label(aggregation_frame, text="Total Trips:")
    total_tools_label = ttk.Label(aggregation_frame, text="Total Tools:")
    total_vehicles_label = ttk.Label(aggregation_frame, text="Total Vehicles:")
    average_trips_traveler_label = ttk.Label(aggregation_frame, text="Average Trips per Traveler:")
    average_trips_companion_label = ttk.Label(aggregation_frame, text="Average Trips per Companion:")
    average_tool_power_label = ttk.Label(aggregation_frame, text="Average Tool Power:")
    average_tool_power_label_after_trip = ttk.Label(aggregation_frame, text="Average Tool Power After Trip:")
    average_vehicle_power_label = ttk.Label(aggregation_frame, text="Average Vehicle Power:")
    average_vehicle_power_label_after_trip = ttk.Label(aggregation_frame, text="Average Vehicle Power After Trip:")

    total_travelers_amt = ttk.Label(aggregation_frame, text=total_travlers)
    total_companions_amt = ttk.Label(aggregation_frame, text=total_companions)
    total_trip_amt = ttk.Label(aggregation_frame, text=total_trips)
    total_tool_amt = ttk.Label(aggregation_frame, text=total_tools)
    total_vehicle_amt = ttk.Label(aggregation_frame, text=total_vehicles)
    trip_traveler_avg = ttk.Label(aggregation_frame, text=average_trips_per_traveler)
    trip_companion_avg = ttk.Label(aggregation_frame, text=average_trips_per_companion)
    tool_power_avg = ttk.Label(aggregation_frame, text=average_tool_power)
    tool_power_avg_after_trip = ttk.Label(aggregation_frame, text=average_tool_power_after_trip)
    vehicle_power_avg = ttk.Label(aggregation_frame, text=average_vehicle_power)
    vehicle_power_avg_after_trip = ttk.Label(aggregation_frame, text=average_vehicle_power_after_trip)

    # Arrage Labels
    total_travelers_label.grid(row = 0, column=0, pady = 0, sticky="E")
    total_companions_label.grid(row = 1, column=0, pady = 0, sticky="E")
    total_trips_label.grid(row = 2, column=0, pady = 0, sticky="E")
    total_tools_label.grid(row = 3, column=0, pady = 0, sticky="E")
    total_vehicles_label.grid(row = 4, column=0, pady = 0, sticky="E")
    average_trips_traveler_label.grid(row = 5, column=0, pady = 0, sticky="E")
    average_trips_companion_label.grid(row = 6, column=0, pady = 0, sticky="E")
    average_tool_power_label.grid(row = 7, column=0, pady = 0, sticky="E")
    average_tool_power_label_after_trip.grid(row = 8, column=0, pady = 0, sticky="E")
    average_vehicle_power_label.grid(row = 9, column=0, pady = 0, sticky="E")
    average_vehicle_power_label_after_trip.grid(row = 10, column=0, pady = 0, sticky="E")

    total_travelers_amt.grid(row = 0, column = 1, pady = 0, sticky="W")
    total_companions_amt.grid(row = 1, column = 1, pady = 0, sticky="W")
    total_trip_amt.grid(row = 2, column = 1, pady = 0, sticky="W")
    total_tool_amt.grid(row = 3, column = 1, pady = 0, sticky="W")
    total_vehicle_amt.grid(row = 4, column = 1, pady = 0, sticky="W")
    trip_traveler_avg.grid(row = 5, column = 1, pady = 0, sticky="W")
    trip_companion_avg.grid(row = 6, column = 1, pady = 0, sticky="W")
    tool_power_avg.grid(row = 7, column = 1, pady = 0, sticky="W")
    tool_power_avg_after_trip.grid(row = 8, column=1, pady = 0, sticky="E")
    vehicle_power_avg.grid(row = 9, column = 1, pady = 0, sticky="W")
    vehicle_power_avg_after_trip.grid(row = 10, column = 1, pady = 0, sticky="W")

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
    submission_button = ttk.Button(export_frame, text="Generate Database Report", command=lambda: generate_database_report())
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

    style = ThemedStyle(root)
    style.set_theme("black")
    style.configure("TLabel", foreground=Constants.GOLD_GALLIFREYAN,background = Constants.BLUE_TARDIS)
    style.configure("TButton", foreground=Constants.CHARCOAL_SONIC_SHADOW,background=Constants.PINK_COMPANION_ROSE)
    style.configure("TFrame", background=Constants.BLUE_TARDIS)
    style.configure("TEntry", foreground="green")
    style.configure("TCombobox", foreground="red")
    style.configure("TTreeview", foreground="orange")
    style.configure("Treeview", foreground=Constants.SILVER_TIME_MIST,background=Constants.PURPLE_NEBULA,fieldbackground=Constants.BLUE_TARDIS)
    style.configure("Treeview.Heading", foreground="pink",background=Constants.BLUE_TARDIS)


    style.configure("TNotebook",background=Constants.PURPLE_NEBULA)
    # Customize notebook tabs
    style.configure("TNotebook.Tab",
                    background="#003B6F",  # Unselected tab background (TARDIS Blue)
                    foreground="white",)  # Unselected tab text
    style.map("TNotebook.Tab",
              background=[("selected", Constants.GOLD_GALLIFREYAN)],  # Selected tab background (Gallifreyan Gold)
              foreground=[("selected", "black")])  # Selected tab text

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