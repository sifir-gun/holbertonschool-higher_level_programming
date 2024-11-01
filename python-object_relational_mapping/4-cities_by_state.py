#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.

Usage: ./4-cities_by_state.py <mysql_username> <mysql_password>
<database_name>
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Vérifier le nombre d'arguments
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql_username>"
              " <mysql_password> <database_name>")
        sys.exit(1)

    # Se connecter à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],     # Nom d'utilisateur MySQL
        passwd=sys.argv[2],   # Mot de passe MySQL
        db=sys.argv[3]        # Nom de la base de données
    )

    # Créer un curseur pour interagir avec la base de données
    cursor = db.cursor()

    # Exécuter la requête SQL
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")
    cursor.execute(query)

    # Récupérer tous les résultats
    rows = cursor.fetchall()

    # Afficher les résultats
    for row in rows:
        print(row)

    # Fermer le curseur et la connexion à la base de données
    cursor.close()
    db.close()
