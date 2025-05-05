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

        print('connection made...')

        return
    
    # Load MySQL configuration from configuration file.
    def get_mysql_config(self):
        with open('config.json', 'r') as file:
            config = json.load(file)
        return config.get('mysql', {})
    
    # On deletion, clean up connection.
    def destructor(self):
        self.cursor.close()
        self.connection.close()
        print("connection closed... goodbye!")