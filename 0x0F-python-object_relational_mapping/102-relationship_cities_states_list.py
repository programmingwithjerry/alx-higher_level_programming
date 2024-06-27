#!/usr/bin/python3
"""
   a script that lists all City objects from the database hbtn_0e_101_usa
"""
from sys import argv
from sqlalchemy import create_engine, and_, text, tuple_
from sqlalchemy.orm import sessionmaker, relationship

from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    if len(argv) >= 4:
        user = argv[1]
        pwd = argv[2]
        db_name = argv[3]
        DATABASE_URL = 'mysql://{}:{}@localhost:3306/{}'.format(
            user, pword, db_name
        )
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        q = session.query(City).join(State).order_by(City.id.asc())
        for city in q.all():
            print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
