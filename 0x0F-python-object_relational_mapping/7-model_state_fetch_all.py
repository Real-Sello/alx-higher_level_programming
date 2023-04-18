#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# Check if the script was executed correctly with 3 arguments
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {} <mysql username> <mysql password> <database name>'
              .format(sys.argv[0]))
        sys.exit(1)

    # Get the MySQL username, password, and database
    # name from the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine to connect to the MySQL server on localhost:3306 with
    # the given credentials and database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Create the tables in the database if they don't already exist
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects from the database, ordered by their ids
    # in ascending order
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print('{}: {}'.format(state.id, state.name))
