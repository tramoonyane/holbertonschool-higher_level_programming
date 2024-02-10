#!/usr/bin/python3

"""
This module contains a function to insert a line of text to a file
after each line containing a specific string.
"""

def append_after(filename="", search_string="", new_string=""):
     """
    Inserts a line of text to a file after each line containing a specific string.

    :param filename: The name of the file to be modified.
    :param search_string: The string to search for in each line.
    :param new_string: The string to be inserted after each line containing the search string.
    """
    # Check if any of the parameters is missing
    if not filename or not search_string or not new_string:
        print("Please provide valid inputs for filename, search_string, and new_string.")
        return

    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Open the file in write mode
    with open(filename, 'w') as file:
        # Iterate through the lines
        for line in lines:
            # Write the current line to the file
            file.write(line)
            
            # Check if the search string is present in the current line
            if search_string in line:
                # If found, append the new string after the line
                file.write(new_string + '\n')
