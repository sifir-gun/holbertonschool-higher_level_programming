#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Création d'un curseur pour exécuter la requête
    cursor = db.cursor()
    
    # Requête SQL pour obtenir les villes avec leurs états correspondants
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)
    
    # Récupération et affichage des résultats
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
