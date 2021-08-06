#!/usr/bin/python3
""" This script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa.

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
    a = session.query(State).filter(State.name == sys.argv[4]).all()
    if a == []:
        print("Not found")
    else:
        for i in a:
            print("{}".format(i.id))
    session.close()
