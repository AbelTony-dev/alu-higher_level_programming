#!/usr/bin/python3
"""module documentation"""

import MySQLdb
import sys


if __name__ == '__main__':
    # Get MySQL username, password and database name
    mysql_username, mysql_password, database_name = sys.argv[1:]

    # Connect to MySQL server on localhost at port 3306
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute SQL query to retrieve all states with a name starting with N
    cursor.execute(
        "SELECT * FROM states "
        "WHERE BINARY name LIKE 'N%' "
        "ORDER BY id ASC"
    )

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    conn.close()
