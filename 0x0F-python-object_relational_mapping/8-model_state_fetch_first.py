#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa:

    -Our script takes 3 arguments:
        -mysql username
        -mysql password
        -database name
    -We use the module SQLAlchemy
    -We import State and Base from model_state
        - from model_state import Base, State
    -Our script connects to a MySQL server running on localhost at port 3306
    -If the table states is empty, print Nothing followed by a new line
    -Our code should not be executed when imported
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Get the MySQL username, password, and database name from the command
    # line arguments
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

    # Query the first State object from the database, ordered by their ids
    # in ascending order
    state = session.query(State).order_by(State.id).first()

    # Print the result, or 'Nothing' if the table is empty
    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')
