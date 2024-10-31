#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute the query to select states starting with 'N'
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )

    # Fetch and display the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
