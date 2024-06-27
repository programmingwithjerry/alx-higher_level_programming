#!/usr/bin/python3
"""
This is the city Relationship
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    n_state = "California"
    n_city = "San Francisco"

    new_state = State(name=nstate)

    new_city = City(name=ncity, state=newState)

    session.add(newCity)

    session.commit()

    session.close()
