#!/usr/bin/python3
"""
script that prints the State object with the name passed as
    argument from the database hbtn_0e_6_usa

    -Our script takes 4 arguments:
        -mysql username
        -mysql password
        -database name
        -state name to search (SQL injection free)
    -We use the module SQLAlchemy
    -We import State and Base from model_state
        - from model_state import Base, State
    -Our script connects to a MySQL server running on localhost at port 3306
    -We assume we have one record with the state name to search
    -Results must display the states.id
    -If no state has the name we searched for, display Not found
    -Our code should not be executed when imported
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """ Prints the State object with the name passed as an argument """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    # Connect to the database using credentials provided
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Using the engine to create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for a State object with the specified name
    state = session.query(State).filter(State.name == name).first()

    # Print State id or Not found if there is no match
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
