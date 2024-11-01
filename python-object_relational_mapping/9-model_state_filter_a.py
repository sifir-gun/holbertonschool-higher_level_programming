#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database
hbtn_0e_6_usa.

Usage: ./9-model_state_filter_a.py <mysql_username> <mysql_password>
                                   <database_name>
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # Create engine and connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query State objects that contain the letter 'a', sorted by id
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
