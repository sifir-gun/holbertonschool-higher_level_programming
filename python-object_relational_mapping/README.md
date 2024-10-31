# Python Object-Relational Mapping

## Description

Dans ce projet, nous lions deux mondes fascinants : **les bases de données** et **Python** ! Ce projet est divisé en deux parties :

1. **Première partie** : utilisation du module `MySQLdb` pour se connecter à une base de données MySQL et exécuter des requêtes SQL.
2. **Seconde partie** : utilisation de `SQLAlchemy`, un **Object Relational Mapper (ORM)**, pour interagir avec la base de données via des objets Python au lieu d'écrire du SQL.

L'objectif d'un ORM est de simplifier l'interaction avec la base de données en se concentrant sur ce qu'on peut faire avec des objets, sans se préoccuper de la façon dont ils sont stockés. Ce projet permet d'approfondir cette approche et de mieux comprendre comment transformer les données entre une base de données relationnelle et des objets Python.

## Prérequis

- **MySQL 8.0** : Assurez-vous que votre serveur MySQL est en version 8.0.
- **Modules Python requis** :
  - `MySQLdb` (version 2.0.x)
  - `SQLAlchemy` (version 1.4.x)
- **Python 3.8+** : Les scripts sont testés sous Ubuntu 20.04 LTS avec Python 3.8.5.

## Installation des dépendances

### Installation de MySQL 8.0

```bash
sudo apt update
sudo apt install mysql-server
mysql --version  # Pour vérifier la version installée
```

### Connexion à MySQL

```bash
sudo mysql
# Sortir avec la commande `quit;`
```

### Installation de MySQLdb et SQLAlchemy

Assurez-vous d'avoir les paquets de développement requis :

```bash
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev

# Pour MySQLdb
sudo pip3 install mysqlclient

# Pour SQLAlchemy
sudo pip3 install SQLAlchemy
```

## Exemples de Code

### Sans ORM

```python
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

### Avec ORM (SQLAlchemy)

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

engine = create_engine('mysql+mysqldb://root:root@localhost/my_db', pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print(f"{state.id}: {state.name}")
session.close()
```

## Objectifs d'apprentissage

À la fin de ce projet, vous devez être capable de :

- Vous connecter à une base de données MySQL depuis un script Python
- Exécuter des requêtes SQL SELECT et INSERT depuis Python
- Comprendre le concept d'ORM
- Mapper une classe Python à une table MySQL

## Structure du projet

| Fichier | Description |
|---------|-------------|
| 0-select_states.py | Liste tous les états de la base de données hbtn_0e_0_usa |
| 1-filter_states.py | Filtre les états commençant par "N" |
| 2-my_filter_states.py | Filtre les états selon une entrée utilisateur |
| 3-my_safe_filter_states.py | Filtrage SQL sécurisé pour éviter les injections |
| 4-cities_by_state.py | Liste toutes les villes avec leur état correspondant |
| 5-filter_cities.py | Liste les villes d'un état donné |
| model_state.py | Contient la classe State pour mapper la table states |
| 7-model_state_fetch_all.py | Liste tous les objets State dans la base de données |
| 8-model_state_fetch_first.py | Affiche le premier objet State de la base de données |
| 9-model_state_filter_a.py | Liste tous les objets State contenant la lettre 'a' |
| 10-model_state_my_get.py | Recherche un état par son nom |
| 11-model_state_insert.py | Ajoute un nouvel état à la base de données |
| 12-model_state_update_id_2.py | Met à jour le nom de l'état avec un ID de 2 |
| 13-model_state_delete_a.py | Supprime les objets State contenant la lettre 'a' |
| 14-model_city_fetch_by_state.py | Liste toutes les villes de chaque état |
| model_city.py | Contient la classe City pour mapper la table cities |

## Notes supplémentaires

Pour éviter les erreurs SQL, les scripts utilisent MySQLdb pour les connexions directes et SQLAlchemy pour les interactions basées sur les objets.

Profitez de ce projet pour approfondir l'utilisation des bases de données et découvrir la puissance des ORM en Python !
