#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    got_it = 0
    for state in session.query(State):
        if sys.argv[4] == state.name:
            print("{}".format(state.id))
            got_it = 1
    if got_it == 0:
        print("Not found")
