#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from the
database hbtn_0e_6_usa.

Usage: ./13-model_state_delete_a.py <mysql_username> <mysql_password>
<database_name>
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <mysql_username>"
              " <mysql_password> <database_name>")
        sys.exit(1)

    # Create engine and connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State objects containing 'a' in their name
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')).all()

    # Delete each state in the list
    for state in states_to_delete:
        session.delete(state)

    # Commit the session to apply the changes
    session.commit()

    # Close the session
    session.close()
