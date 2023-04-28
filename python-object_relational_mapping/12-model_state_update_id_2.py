#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Connecting with database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creating session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Updating state
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'

    # Committing changes
    session.commit()

    # Closing session
    session.close()
