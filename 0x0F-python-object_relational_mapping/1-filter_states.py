#!/usr/bin/python3
"""
script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa:
    -Our script takes 3 arguments:
        -mysql username
        -mysql password
        -database name (no argument validation needed)
    -We use the module MySQLdb (import MySQLdb)
    -Our script connects to a MySQL server running on localhost at port 3306
    -Results must be sorted in ascending order by states.id
    -Results must be displayed as they are in the example below
    -Our code should not be executed when imported
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # get MySQL username, password, and database
    # name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    # create a cursor object to execute SQL queries
    cursor = db.cursor()

    # execute SQL query to select all states with names
    # starting with "N", ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # iterate over query results and print each row mathing the query
    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == "N":
            print(row)

    # close the database connection
    db.close()
