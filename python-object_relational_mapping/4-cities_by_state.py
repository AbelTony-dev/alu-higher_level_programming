#!/usr/bin/python3
"""module documentation"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Open database connection
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # prepare a cursor object
    cursor = db.cursor()

    # execute SQL query
    cursor.execute('SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    JOIN states\
                    ON cities.state_id = states.id\
                    ORDER BY cities.id ASC')

    # fetch all rows
    rows = cursor.fetchall()

    # print out the results
    for row in rows:
        print(row)

    # disconnect from server
    db.close()
