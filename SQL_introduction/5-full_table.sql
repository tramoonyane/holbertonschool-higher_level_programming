#!/bin/bash

# Script to print the description of the table first_table from the database hbtn_0c_0 in MySQL server

# Check if the required argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

# Assign the argument to a variable
database=$1

# MySQL query to retrieve table structure
echo "SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_KEY, EXTRA
           FROM INFORMATION_SCHEMA.COLUMNS
           WHERE TABLE_SCHEMA = '$database' AND TABLE_NAME = 'first_table';"
