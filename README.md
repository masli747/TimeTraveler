# Time Traveler Log App – CPSC 408

Authors: Zack Corr, Mason Li, Lauren Yeretzian  
Course: CPSC 408 – Database Management  
Project: Final Project – Time Traveler Log App

## Description:
This application serves as a fictional sci-fi database for time travelers to log and manage their adventures through time.

Users can:
- Document their trips, companions, vehicles, and tools.
- Track time travelers, their trips, companions, tools, and vehicles.
- Log details, view statistics, and generate reports for their trips.

Overall, it works as a digital, time-traveling diary!

## Tech Stack:
- Frontend: Tkinter
- Backend: MySQL

## How to Run:
1. Set up the MySQL Database:
   - Open your MySQL client and run TimeTravelingSchema.sql;

     This will:
     - Create the "timetraveler" database.
     - Set up the schema and load some test data

2. Make sure you hve the needed packages
- Run in terminal the following commands:
    - pip install pandas
    - pip install ttkthemes

3. Run the Tkinter Application:
   - Navigate to the project folder containing the interface script.
   - Run the main Python script:
     python app.py

   - A Tkinter window will open. Use the buttons and forms to interact with the database through the app UI.

## Project Files:

- timetravelerSchema.sql
- app.py
- constants.py
- controller.py
- db_operations.py
- helper.py
- ERDiagram.png
- README.txt          

## Database Login Info:

db_operations uses config.json with a sample login to access a MySQL local server. This is insecure and should be changed in your own configuration.
- user: root
- password: CPSC408!

## Known Errors

N/A

## Outside Sources Used:

1. Help on themes and formatting in Tkinter
- Source: "ttkthemes documentation"
- URL: https://ttkthemes.readthedocs.io/en/latest/

2. Referencing StackOverflow for general implementation questions/Help
- Source: StackOverflow
- URL: https://stackoverflow.com/questions

3. Occasional debug help from ChatGPT, on stubborn debug issues past the scope of this course
- Source: ChatGPT (o3 model)
- URL: https://openai.com/

4. Python Grid() method in Tkinter
- Source: GeeksForGeeks
- URL: https://www.geeksforgeeks.org/python-grid-method-in-tkinter/

5. Configure widgets in Python-Tkinter
- Source: Coders Legacy
- URL: https://coderslegacy.com/python/tkinter-config/

6. Events in binds in Tkinter
- Source: Python Course
- URL: https://python-course.eu/tkinter/events-and-binds-in-tkinter.php

7. Setting up TkDocs
- Source: TkDocs.com
- URL: https://tkdocs.com/tutorial/tree.html

8. Clear entire Treeview with Tkinter
- Source: Tutorials Point
- URL: https://www.tutorialspoint.com/how-to-clear-an-entire-treeview-with-tkinter

9. Formatting column names using Tkinter integration
- Source: MySQL developers forum
- URL: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-column-names.html

10. Using asksaveasfile() file in Tkinter
- Source: GeeksForGeeks
- URL: https://www.geeksforgeeks.org/python-asksaveasfile-function-in-tkinter/

