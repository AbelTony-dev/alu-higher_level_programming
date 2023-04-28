#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and session factory
    db_url = "mysql+mysqldb://" + mysql_username +\
             ":" + mysql_password + "@" + \
             "localhost:3306/" + database_name
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query for all State objects
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
