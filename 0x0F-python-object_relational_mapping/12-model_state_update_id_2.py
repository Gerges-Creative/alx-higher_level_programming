#!/usr/bin/python3
"""
update state: given id, change state name
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

    # Query the State table to find the state with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the name of the state
    state_to_update.name = "New Mexico"
    session.commit()

    session.close()
