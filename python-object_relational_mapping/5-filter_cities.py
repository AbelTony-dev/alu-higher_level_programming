#!/usr/bin/python3
"""documentation"""

import MySQLdb
import sys


if __name__ == '__main__':
    # Get MySQL username, password, database name, and state
    mysql_username, mysql_password, database_name, state_name = sys.argv[1:]

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

    # Execute SQL query to retrieve all cities of the given state
    cursor.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,)
    )

    # Fetch all rows and print them
    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    # Close cursor and database connection
    cursor.close()
    conn.close()
