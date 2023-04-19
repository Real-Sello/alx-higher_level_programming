#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Deletes states from the database"""
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to MySQL server running on localhost
    # at port 3306
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database))

    # Using engine to create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to find all State objects with a name
    # containing the letter a
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Loop through the results and delete each object
    for state in states_with_a:
        session.delete(state)

    # Commit the changes to the database and close the session
    session.commit()
    session.close()
