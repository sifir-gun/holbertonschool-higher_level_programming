#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N' from the database hbtn_0e_0_usa
Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the database using provided arguments
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
