#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == '__main__':
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the query result
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connections
    cursor.close()
    db.close()
