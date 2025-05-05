"""
 * db_operations.py contains methods to interact with the MySQL database.
 * When an instance of db_oprations is created, it immediately attempts to read
 * a password file and connect to the MySQL database.
"""

import mysql.connector

class db_operations:
    def __init__(self):
        # read username + password from file
        # make mysql connection
        return