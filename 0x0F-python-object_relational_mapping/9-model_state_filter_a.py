#!/usr/bin/python3
"""script that lists all State objects that contain the letter a
    from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """ Lists all State objects containing the letter "a" """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database using credentials provided
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database))

    # Using the engine to create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and print all State objects from the 'states' table
    # that contains the letter 'a'
    query = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id)
    for state in query:
        print("{}: {}".format(state.id, state.name))
    session.close()
