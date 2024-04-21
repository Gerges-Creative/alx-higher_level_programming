#!/usr/bin/python3
"""
Defines class State for SQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
"""
Imports from SQLAlchemy
"""

Base = declarative_base()


class State(Base):
    """
    Represents a state in a country.

    Inherits from SQLAlchemy's Base class.

    Attributes:
        id (int): Auto-incremented primary key for the state.
        name (str): Name of the state, limited to 128 characters.
    """
    __tablename__ = "states"
    id = Column(Integer, prinmary_key=True, autoincrement=True)
    name = Column(string(128), nullable=False)
