#!/usr/bin/python3
"""script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # get MySQL username, password, database name, and
    # state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    # create a cursor object to execute SQL queries
    cursor = db.cursor()

    # execute SQL query to select all rows from states
    # table where name matches the state name argument, ordered by id
    query = "SELECT * FROM states WHERE name LIKE BINARY %s\
    ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(query, ('%' + state_name + '%',))

    # iterate over query results and print each row
    for row in cursor.fetchall():
        print(row)

    # close the database connection
    db.close()
