#!/usr/bin/python3
"""a python file that contains the class definition of a
    City and an instance Base = declarative_base()
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
