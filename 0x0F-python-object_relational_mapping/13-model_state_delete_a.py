#!/usr/bin/python3
"""
update state: given id, change state name
parameters given to script: username, password, database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # make engine for database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State table to find the state with 'a' in it
    states_to_delete = session.query(State).filter(
        State.name.like('%a%'))
    for row in states_to_delete:
        if row:
            session.delete(row)
    session.commit()

    session.close()
