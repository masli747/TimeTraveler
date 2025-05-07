"""
 * db_operations.py contains methods to interact with the MySQL database.
 * When an instance of db_oprations is created, it immediately attempts to read
 * a password file and connect to the MySQL database.
"""

import json
import mysql.connector

class db_operations:
    # Make a connection to the MySQL database upon creation so we can conduct DML/DQL.
    def __init__(self):
        # Get properties for connecting to server.
        config = self.get_mysql_config()
        
        self.connection = mysql.connector.connect(
            host = config.get('host', ''),
            user = config.get('user', ''),
            password = config.get('password', ''),
            auth_plugin = 'mysql_native_password',
            database = config.get('database', '')
        )

        self.cursor = self.connection.cursor()

        # print('connection made...')

        return
    
    # Load MySQL configuration from configuration file.
    def get_mysql_config(self):
        with open('src/config.json', 'r') as file:
            config = json.load(file)
        return config.get('mysql', {})
    
    # Supported operations.
    # DDL/DML
    # function to simply execute a DDL or DML query.
    # commits query, returns no results. 
    # best used for insert/update/delete queries with no parameters
    def modify_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    # function to simply execute a DDL or DML query with parameters
    # commits query, returns no results. 
    # best used for insert/update/delete queries with named placeholders
    def modify_query_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        self.connection.commit()

    # DQL
    # Selects
    # function to simply execute a DQL query
    # does not commit, returns results
    # best used for select queries with no parameters
    def select_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # function to simply execute a DQL query with parameters
    # does not commit, returns results
    # best used for select queries with named placeholders
    def select_query_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        return self.cursor.fetchall()
    
    # Aggregations
    
    # On deletion, clean up connection.
    def destructor(self):
        self.cursor.close()
        self.connection.close()
        # print("connection closed... goodbye!")