#!/usr/bin/env python3
""" Script that prints all City objects from the database hbtn_0e_14_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City


if __name__ == "__main__":
    """Prints city objects from the database"""

    # Create engine to connect to MySQL server running on localhost
    # at port 3306e
    db = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Using engine to create a session
    Session = sessionmaker(bind=db)
    session = Session()

    # Query the database to retrieve all City objects
    # Print results and close session
    for cities, state in session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, cities.id, cities.name))
