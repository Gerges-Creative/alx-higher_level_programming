#!/usr/bin/python3
"""
Defines class State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """
    Class State; instance of Base
    Linked to MySQL table "states"
    """
    __tablename__ = 'states'

    id = Column(Integer, prinmary_key=True, autoincrement=True)
    name = Column(string(128), nullable=False)
