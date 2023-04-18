#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

# Check if the correct number of arguments have been passed to the script
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        # Create a cursor object to execute SQL queries
        cur = db.cursor()

        # Execute an SQL query to retrieve all rows from the "cities" table
        cur.execute("SELECT cities.id, cities.name,\
                      states.name FROM cities\
                      INNER JOIN states\
                      ON states.id=cities.state_id")

        # Fetch all the rows returned by the query
        rows = cur.fetchall()

        # Loop through each row and print it to the console
        for row in rows:
            print(row)

        # Close the cursor and database connection
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        # If there is an error, print the error message
        # and exit the script with a status code of 1
        print("MySQL Error [{}]: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
