#!/usr/bin/python3
"""documentation"""
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

    query = text("""
        SELECT CONCAT(states.name, ': (', cities.id, ') ', cities.name) AS result
        FROM cities
        JOIN states ON cities.state_id = states.id;
    """)

    results = session.execute(query)

    # Print results
    for row in results:
        print(row['result'])

    # Close the session
    session.close()