#!/usr/bin/python3
"""a script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
    -Our script takes 4 arguments:
        -mysql username
        -mysql password
        -database name
        -state name searched (safe from MySQL injection)
    -We use the module MySQLdb (import MySQLdb)
    -Our script connects to a MySQL server running on localhost at port 3306
    -Results must be sorted in ascending order by states.id
    -Results must be displayed as they are in the example below
    -Our code should not be executed when imported
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state = sys.argv[4]

    # connect to database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname, charset="utf8")
    cursor = db.cursor()

    # execute query with safe parameter substitution
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state,))

    # fetch results and print them in the desired format
    results = cursor.fetchall()
    for row in results:
        print(row)

    # close database connection
    db.close()
