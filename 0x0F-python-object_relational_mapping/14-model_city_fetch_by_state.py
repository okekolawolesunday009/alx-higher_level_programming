#!/usr/bin/python3
""" List all state objects using sqlalchemy """
#!/usr/bin/python3
import sqlalchemy
from sys import argv, exit
from model_state import Base, State, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3],
                                  pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).\
            filter(State.id == City.state_id).order_by(City.id):
        print('{}: ({}) {}'.format(state.name, city.id, city.name))