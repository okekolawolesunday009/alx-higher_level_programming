#!/usr/bin/python3
import sqlalchemy 
from sys import argv, exit
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3],
                                  pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()
    stateArr = []
    states = session.query(State).order_by(State.id).all()

    for state in states:
        stateArr.append(state)

    # Print only the first state in stateArr
    if stateArr:
        print("{}: {}".format(stateArr[0].id, stateArr[0].name))
    else:
        print("No states found.")