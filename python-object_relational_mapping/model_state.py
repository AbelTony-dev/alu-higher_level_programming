#!/usr/bin/python3
"""module documentation"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Create a declarative base instance
Base = declarative_base()


# Define the State class
class State(Base):
    """State class that links to the MySQL table states"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
