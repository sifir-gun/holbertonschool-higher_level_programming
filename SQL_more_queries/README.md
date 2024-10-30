# SQL More Queries

## Description
Ce projet contient une série de scripts SQL pour effectuer diverses tâches sur un serveur MySQL. Chaque script aborde un aspect spécifique des requêtes SQL avancées, des autorisations des utilisateurs à la manipulation de tables et à la gestion des relations entre les données. 

Les scripts permettent de créer des utilisateurs, gérer les privilèges, manipuler les bases de données et les tables, et réaliser des requêtes complexes pour afficher des données spécifiques.

## Contenu des Fichiers

- **0-privileges.sql** : Liste tous les privilèges des utilisateurs `user_0d_1` et `user_0d_2` sur le serveur MySQL.
- **1-create_user.sql** : Crée l'utilisateur `user_0d_1` avec tous les privilèges sur le serveur MySQL.
- **2-create_read_user.sql** : Crée la base de données `hbtn_0d_2` et l'utilisateur `user_0d_2` avec uniquement le privilège `SELECT` sur cette base de données.
- **3-force_name.sql** : Crée une table `force_name` où le champ `name` ne peut pas être nul.
- **4-never_empty.sql** : Crée une table `id_not_null` où `id` a une valeur par défaut de `1`.
- **5-unique_id.sql** : Crée une table `unique_id` où `id` doit être unique et a une valeur par défaut de `1`.
- **6-states.sql** : Crée la base de données `hbtn_0d_usa` et la table `states` avec un `id` unique, auto-généré, et `name` non nul.
- **7-cities.sql** : Crée la table `cities` dans la base de données `hbtn_0d_usa` avec une clé étrangère `state_id` référant à `states`.
- **8-cities_of_california_subquery.sql** : Liste toutes les villes de Californie de la base de données `hbtn_0d_usa`.
- **9-cities_by_state_join.sql** : Liste toutes les villes contenues dans la base de données `hbtn_0d_usa` avec leur état associé.
- **10-genre_id_by_show.sql** : Liste tous les shows qui ont au moins un genre lié dans la base de données `hbtn_0d_tvshows`.
- **11-genre_id_all_shows.sql** : Liste tous les shows de la base de données `hbtn_0d_tvshows` avec leur `genre_id`, même si aucun genre n'est associé.
- **12-no_genre.sql** : Liste tous les shows qui n'ont pas de genre lié dans la base de données `hbtn_0d_tvshows`.
- **13-count_shows_by_genre.sql** : Liste tous les genres et le nombre de shows liés pour chaque genre dans la base de données `hbtn_0d_tvshows`.
- **14-my_genres.sql** : Liste tous les genres associés au show `Dexter` dans la base de données `hbtn_0d_tvshows`.
- **15-comedy_only.sql** : Liste tous les shows de genre `Comedy` dans la base de données `hbtn_0d_tvshows`.
- **16-shows_by_genre.sql** : Liste tous les shows et les genres liés, même si un show n'a pas de genre, dans la base de données `hbtn_0d_tvshows`.

## Prérequis
- Serveur MySQL installé.
- Accès à un utilisateur `root` pour l'exécution des scripts.
- Les bases de données `hbtn_0d_2` et `hbtn_0d_usa` doivent être créées pour certains exercices.

## Utilisation
Pour exécuter les scripts, utilisez la commande suivante en remplaçant le fichier et la base de données selon le besoin :

```bash
cat <fichier>.sql | mysql -hlocalhost -uroot -p <nom_base_de_donnees>
