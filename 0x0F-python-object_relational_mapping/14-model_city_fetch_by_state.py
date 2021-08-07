#!/usr/bin/python3
""" This script that prints all City objects from the database hbtn_0e_14_usa.

"""


from sqlalchemy import (create_engine)
from sqlalchemy.orm.session import Session
from model_state import Base, State
from model_city import City
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1],
                            sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    a = session.query(City).order_by(City.id).join(State)
    for i in a:
        print("{}: ({}) {}".format(i.state.name, i.id, i.name))
    session.close()
