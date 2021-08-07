#!/usr/bin/python3
""" State class.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ This class inherits of the Base class and create:
    1-> An tabla called states.
    2-> two columns called id and name.

    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
