#!/usr/bin/python3
"""
Add a new state to the database.
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

    new_state_name = "Louisiana"
    new_state = State(name=new_state_name)
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()

