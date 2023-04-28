#!/usr/bin/python3
"""module documentation"""

import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306,
        charset="utf8"
    )

    cur = db.cursor()
    query = "SELECT * FROM states " \
        "WHERE name LIKE BINARY '{}' " \
        "ORDER BY id ASC".format(search)
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
