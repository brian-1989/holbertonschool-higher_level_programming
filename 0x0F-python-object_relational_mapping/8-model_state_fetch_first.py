#!/usr/bin/python3
""" This script prints the first State object from the database hbtn_0e_6_usa.

"""


from sqlalchemy import (create_engine)
from sqlalchemy.orm.session import Session
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1],
                            sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    a = session.query(State).first()
    if State:
        print("{}: {}".format(a.id, a.name))
    else:
        print("Nothing")
    session.close()
