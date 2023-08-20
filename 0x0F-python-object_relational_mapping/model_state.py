#!/usr/bin/python3
"""script containing the class definition of a
State and an instance Base = declarative_base():

State class:
    inherits from Base Tips
    links to the MySQL table states
    class attribute id that represents a column of an auto-generated,
        unique integer, can’t be null and is a primary key
    class attribute name that represents a column of a string with
        maximum 128 characters and can’t be null
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base instance
Base = declarative_base()


# Define the State class, which inherits from Base
class State(Base):
    """
    A class for linking the States table.
    """
    # Specify the name of the MySQL table that corresponds
    # to the State class
    __tablename__ = 'states'

    # Define the id and name columns
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
