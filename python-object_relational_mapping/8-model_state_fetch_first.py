#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.

Usage: ./8-model_state_fetch_first.py <mysql_username> <mysql_password>
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

    # Query the first State object ordered by states.id
    state = session.query(State).order_by(State.id).first()

    # Display the result
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
