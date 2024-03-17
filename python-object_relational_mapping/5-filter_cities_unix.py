#!/usr/bin/python3
"""
Script to list all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

def filter_cities_by_state(username, password, database, state_name):
    """
    Connects to the MySQL server and lists all cities of the specified state.
    
    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to search for cities.
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()
        query = """
            SELECT GROUP_CONCAT(name SEPARATOR ', ')
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """
        cursor.execute(query, (state_name,))
        cities = cursor.fetchone()[0]
        if cities:
            print(cities)
        else:
            print("No cities found for the state:", state_name)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: ./5-filter_cities.py <username> <password> <database> <state_name>")
