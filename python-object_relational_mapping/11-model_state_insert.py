#!/usr/bin/python3
"""
Adds the State object 'Louisiana' to the database hbtn_0e_6_usa.

Usage: ./11-model_state_insert.py <mysql_username> <mysql_password>
<database_name>
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <mysql_username>"
              "<mysql_password> <database_name>")
        sys.exit(1)

    # Create engine and connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create all tables in the engine (if not already created)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a new State object
    new_state = State(name='Louisiana')

    # Add the new State object to the session
    session.add(new_state)

    # Commit the session to write the changes to the database
    session.commit()

    # Print the new state's id
    print(f"{new_state.id}")

    # Close the session
    session.close()
