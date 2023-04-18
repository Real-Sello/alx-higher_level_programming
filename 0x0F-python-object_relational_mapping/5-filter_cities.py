#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Retrieve the MySQL credentials and state
    # name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    # Connect to the MySQL server using the provided
    # credentials and database name
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Use a single execute statement to retrieve and join the cities
    # in the specified state, sorted in ascending order by city ID
    cur.execute("SELECT cities.id, cities.name,\
                      states.name FROM cities\
                      INNER JOIN states\
                      ON states.id=cities.state_id")
    # fetch all rows returned by the query
    rows = cur.fetchall()

    # Iterate through row and print ID and Name
    myList = []
    for row in rows:
        if row[2] == state:
            myList.append(row[1])
    print(", ".join(myList))

    # Close the cursor and database connection
    cur.close()
    db.close()
