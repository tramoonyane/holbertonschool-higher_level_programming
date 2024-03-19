#!/usr/bin/python3
"""
Script to display all values in the
states table of hbtn_0e_0_usa
where name matches the provided argument.
"""

import MySQLdb
import sys


def filter_states_by_name(username, password, database, state_name):
    """
    Connects to the MySQL server and displays
    all rows in the states table
    where the name matches the provided argument.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to search for.
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        # Create a cursor object
    cursor = conn.cursor()

    # SQL query with user input using format
    query = "SELECT * FROM states WHERE name LIKE '{}%'
    ORDER BY id ASC".format(state_name)

    # Execute the query
    cursor.execute(query)

    # Fetch all the matching rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the connection
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password>
        <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]
    display_states_by_name(username, password, database, state_name)
