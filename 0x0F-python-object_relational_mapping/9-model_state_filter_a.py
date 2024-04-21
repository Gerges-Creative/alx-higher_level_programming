#!/usr/bin/python3
"""
return state objects containing letter 'a' from database via python
parameters given to script: username, password, database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # make engine for database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).where(
        State.name.like("%a%")).order_by(State.id)
    # query python instance in database for letter 'a'
    for row in results:
        print("{}: {}".format(row.id, row.name))

    session.close()
