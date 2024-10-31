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
    
    # Exécution de la requête SQL avec utilisation de %s pour éviter les injections SQL
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))
    
    # Récupération et affichage des résultats
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
