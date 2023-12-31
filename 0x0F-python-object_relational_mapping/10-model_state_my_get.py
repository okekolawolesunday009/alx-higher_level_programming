#!/usr/bin/python3
"""documentatio"""
import sqlalchemy
from sys import argv, exit
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3], argv[4],
                                  pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(
            State.name == argv[4]).first()

    if states is not None:
        print("{}".format(states.id))
    else:
        print("Not found")
