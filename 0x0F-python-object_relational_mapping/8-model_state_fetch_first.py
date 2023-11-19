#!/usr/bin/python3
"""documentation"""


if __name__ == '__main__':

    import sqlalchemy
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker, Session

    username = '{}'.format(argv[1])
    password = '{}'.format(argv[2])
    db_name = '{}'.format(argv[3])

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).first()

    if states is not None:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")
