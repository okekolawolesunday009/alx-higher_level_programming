#!/usr/bin/python3
"""documentation"""
import sqlalchemy
from sys import argv, exit
from model_state import Base, State
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3],
                                  pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    stateArr = []
    states = insert(State).values(name="Louisiana")
    states = session.query(State).filter(State.name == "Louisiana"
                                         ).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))