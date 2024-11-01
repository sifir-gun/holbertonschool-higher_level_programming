#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N' from the database hbtn_0e_0_usa
Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données avec les arguments fournis
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = db.cursor()

    # Exécution de la requête SQL pour récupérer les états dont le nom commence par "N"
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")
    rows = cursor.fetchall()

    # Affichage des résultats
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    db.close()
