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

    # add new state and commit to table
    ins = State(name='Louisiana')
    session.add(ins)
    session.commit()
    results = session.query(State).filter(State.name == "Louisiana").first()
    if results:
        print("{}".format(results.id))

    session.close()
