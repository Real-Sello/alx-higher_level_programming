#!/usr/bin/python3
"""a python file that contains the class definition of a
    State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base instance
Base = declarative_base()

# Define the State class, which inherits from Base
class State(Base):
    """
    A class for linking the cities table.
    """
    # Specify the name of the MySQL table that corresponds to the State class
    __tablename__ = 'states'

    # Define the id and name columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

