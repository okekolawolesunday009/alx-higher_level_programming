#!/usr/bin/python3
"""Start link class to table in database 
"""
"""documnetation"""
import MySQLdb
from sys import argv, exit
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
