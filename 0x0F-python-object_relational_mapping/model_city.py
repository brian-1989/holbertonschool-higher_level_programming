#!/usr/bin/python3
""" City class.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from model_state import State

Base = declarative_base()


class City(Base):
    """ This class inherits of the Base class, serve to connect
    the states and cities tables and create:
    1-> An table called cities.
    2-> three columns called id, name and state_id

    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))
    # It is used to connect a variable with the states table
    # and can access the columns of said table
    state = relationship(State)
