#!/usr/bin/python3
"""
   This script lists all State objects
   from the database `hbtn_0e_6_usa`.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Gain access to the database and get the states
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))
