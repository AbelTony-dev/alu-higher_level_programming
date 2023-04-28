#!/usr/bin/python3
# Import necessary modules
"""module documentation"""
import MySQLdb
import sys

# Connect to MySQL database using command-line arguments
if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to select all states and order by id
    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    # Fetch all rows and print them out
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connections
    cursor.close()
    db.close()
