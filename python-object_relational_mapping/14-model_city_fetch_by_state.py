#!/usr/bin/python3
"""
Affiche tous les objets City de la base de données hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Vérifier le nombre d'arguments
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <mysql_username>"
              "<mysql_password> <database_name>")
        sys.exit(1)

    # Créer l'engine et se connecter à la base de données
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Créer une session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour joindre les tables State et City
    results = session.query(
        State, City).filter(State.id == City.state_id).order_by(City.id).all()

    # Afficher les résultats
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Fermer la session
    session.close()
