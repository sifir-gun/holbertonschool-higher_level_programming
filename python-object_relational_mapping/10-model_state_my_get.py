#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from the database
hbtn_0e_6_usa.

Usage: ./10-model_state_my_get.py <mysql_username> <mysql_password>
                                  <database_name> <state_name>
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # Check for correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql_username>"
              " <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    # Create engine and connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Get the state name to search, avoiding SQL injection
    state_name = sys.argv[4]

    # Query the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Display the result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
