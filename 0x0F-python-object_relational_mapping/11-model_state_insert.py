#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa:

    -Our script takes 3 arguments:
        -mysql username
        -mysql password
        -database name
    -We use the module SQLAlchemy
    -We import State and Base from model_state
        - from model_state import Base, State
    -Our script connects to a MySQL server running on localhost at port 3306
    -Print the new states.id after creation
    -Our code should not be executed when imported
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """ Adds the State object "Louisiana" to the database """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object and add it to the session
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)
    session.close()
