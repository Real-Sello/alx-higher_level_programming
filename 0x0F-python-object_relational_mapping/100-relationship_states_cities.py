#!/usr/bin/python3
"""
script that creates the State 'California' with the City 'San Francisco'
from the database hbtn_0e_100_usa:
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    # Check if correct number of arguments has been provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the connection URL
    connection_url = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(mysql_username, mysql_password, database_name)

    # Create the engine
    engine = create_engine(connection_url)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State 'California'
    california = State(name="California")

    # Create the City 'San Francisco' and associate it with 'California'
    san_francisco = City(name="San Francisco", state=california)
    california.cities.append(san_francisco)

    # Add 'California' and 'San Francisco' to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
