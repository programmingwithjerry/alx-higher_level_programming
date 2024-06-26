#!/usr/bin/python3
"""
   a script that changes the name of a State object
   from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_id = 2
    new_state_name = "New Mexico"

    states_to_update = session.query(State).filter(State.id == state_id)
    for state in states_to_update:
        state.name = new_state_name

    session.commit()

    session.close()

