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
    
    # Requête pour sélectionner les états commençant exactement par 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    
    # Affichage des résultats
    rows = cursor.fetchall()

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
