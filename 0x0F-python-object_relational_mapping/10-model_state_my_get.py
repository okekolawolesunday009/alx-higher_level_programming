#!/usr/bin/python3
import sqlalchemy
from sys import argv, exit
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3], argv[4],
                                  pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()
    stateArr = []
    states = session.query(State).filter(
            State.name == argv[4]).order_by(State.id).all()

    for state in states:
        print("{}".format(state.id))
    else:
        print("Not found")
