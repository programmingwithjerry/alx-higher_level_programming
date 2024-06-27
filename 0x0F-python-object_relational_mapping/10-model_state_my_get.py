#!/usr/bin/python3
"""
This script prints the ID of the State object
with the name provided as an argument
from the database `hbtn_0e_6_usa`.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database and retrieve a state
    based on the provided name.
    """

    database_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(database_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    state_instance = session.query(State).filter(State.name == sys.argv[4]).first()

    if state_instance is None:
        print('Not found')
    else:
        print('{0}'.format(state_instance.id))

