#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa:

-Our script takes 3 arguments:
    -mysql username
    -mysql password
    -database name
-We use the module SQLAlchemy
-We import State and Base from model_state
    - from model_state import Base, State
-Our script connects to a MySQL server running on localhost at port 3306
-Our code should not be executed when imported
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """ Changes the name of a State object in the database """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database))

    # Using engine to create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to find the State with id=2
    state = session.query(State).filter(State.id == 2).first()

    # Update the state name artribute and commit the change
    state.name = "New Mexico"
    session.commit()
    session.close()
