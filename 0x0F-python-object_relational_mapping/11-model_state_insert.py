#!/usr/bin/python3
""" This script adds the State object “Louisiana” to the
database hbtn_0e_6_usa.

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
    # The object was created
    obj1 = State(name='Louisiana')
    # The object created is add
    session.add(obj1)
    # The object was save in the data base
    session.commit()
    print(obj1.id)
    session.close()
