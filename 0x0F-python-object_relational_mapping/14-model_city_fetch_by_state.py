#!/usr/bin/python3
"""
   Cities in State
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.name, City.id, City.name).\
        join(City, State.id == City.state_id).\
        order_by(City.id)

    records = query.all()

    for record in records:
        print("{:s}: ({:d}) {:s}".format(*record))

    session.close()
