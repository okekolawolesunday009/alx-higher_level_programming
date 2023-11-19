#!/usr/bin/python3
""" List all state objects using sqlalchemy """

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm.session import sessionmaker, Session
from sqlalchemy import create_engine
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3],
                                  pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)

    session.commit()