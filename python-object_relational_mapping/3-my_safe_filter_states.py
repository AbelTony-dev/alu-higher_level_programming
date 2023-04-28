#!/usr/bin/python3
"""module documentation"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Open database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # prepare a cursor object
    cursor = db.cursor()

    # execute SQL query using parameters to avoid SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # fetch all rows
    rows = cursor.fetchall()

    # print out the results
    for row in rows:
        print(row)

    # disconnect from server
    db.close()
