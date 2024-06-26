#!/usr/bin/python3
"""
return all state objects from database via python
parameters given to script: username, password, database
"""

import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # make engine for database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query_result = session.query(City, State).join(
        State).order_by(City.id).all()
    for city, state in query_result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
