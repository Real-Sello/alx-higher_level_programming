#!/usr/bin/python3
"""a python file that contains the class definition of a
    City and an instance Base = declarative_base():
        -City class:
            -inherits from Base (imported from model_state)
            -links to the MySQL table cities
            -class attribute id that represents a column of an auto-generated,
            unique integer, can’t be null and is a primary key
            -class attribute name that represents a column of a string of 128
            characters and can’t be null
            -class attribute state_id that represents a column of an integer,
            can’t be null and is a foreign key to states.id
        -We use the module SQLAlchemy
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base instance
Base = declarative_base()


# Define the City class, which inherits from Base
class City(Base):
    """
    A class for linking the Cities table.
    """
    # Specify the name of the MySQL table that corresponds to the State class
    __tablename__ = 'cities'

    # Define the id, state_id and name columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
