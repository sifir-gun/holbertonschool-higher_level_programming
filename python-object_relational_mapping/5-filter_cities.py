#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa.

Usage: ./5-filter_cities.py <mysql_username> <mysql_password>
                            <database_name> <state_name>
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Vérifier le nombre d'arguments
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <mysql_username> <mysql_password>"
              " <database_name> <state_name>")
        sys.exit(1)

    # Se connecter à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],      # Nom d'utilisateur MySQL
        passwd=sys.argv[2],    # Mot de passe MySQL
        db=sys.argv[3]         # Nom de la base de données
    )

    # Créer un curseur pour interagir avec la base de données
    cursor = db.cursor()

    # Préparer la requête SQL sécurisée contre les injections SQL
    query = ("SELECT cities.name FROM cities"
             " JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY cities.id ASC")
    cursor.execute(query, (sys.argv[4],))

    # Récupérer tous les résultats
    rows = cursor.fetchall()

    # Extraire les noms des villes
    city_names = [row[0] for row in rows]

    # Afficher les noms des villes séparés par une virgule
    print(", ".join(city_names))

    # Fermer le curseur et la connexion à la base de données
    cursor.close()
    db.close()
