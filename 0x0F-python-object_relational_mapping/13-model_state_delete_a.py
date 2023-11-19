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

    updated_state = session.query(State).filter_by(id=2).first()
    if updated_state:
        updated_state.name = "New Mexico"
        session.commit()
        print("State with id 2 updated successfully.")
    else:
        print("State with id 2 not found.")