#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.

Usage: ./12-model_state_update_id_2.py <mysql_username> <mysql_password>
<database_name>
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <mysql_username>"
              "<mysql_password> <database_name>")
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

    # Query the State object with id = 2
    state = session.query(State).filter_by(id=2).first()

    # Check if the state exists
    if state:
        # Update the state's name
        state.name = "New Mexico"
        # Commit the changes
        session.commit()

    # Close the session
    session.close()
