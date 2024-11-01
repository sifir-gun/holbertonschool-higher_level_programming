#!/usr/bin/python3
"""
Lists all states where name matches the argument from the database hbtn_0e_0_usa

Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Vérification du nombre d'arguments
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    # Connexion à la base de données avec les arguments fournis
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = db.cursor()

    # Récupération du nom de l'état recherché
    state_name_searched = sys.argv[4]

    # Exécution de la requête SQL pour récupérer les états dont le nom correspond exactement à celui fourni
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name_searched)
    cursor.execute(query)
    rows = cursor.fetchall()

    # Affichage des résultats
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    db.close()
