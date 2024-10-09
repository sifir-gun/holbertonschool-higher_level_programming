"""
Ce module interagit avec une API pour récupérer des données de posts et les
afficher ou les sauvegarder dans un fichier CSV. Il utilise les bibliothèques
requests pour les requêtes HTTP et csv pour la gestion du fichier CSV.

Fonctions:
- fetch_and_print_posts:
Récupère et affiche les posts depuis l'API JSONPlaceholder.
- fetch_and_save_posts:
Récupère et sauvegarde les posts dans un fichier CSV.
"""
import csv
import requests


def fetch_and_print_posts():
    """
    Récupère les posts de l'API JSONPlaceholder et affiche les titres.

    Cette fonction utilise la méthode GET pour envoyer une requête HTTP à
    l'API JSONPlaceholder. Elle imprime le code de statut de la requête, et si
    la requête réussit, affiche les titres des posts récupérés.

    Si la requête échoue, un message d'erreur est affiché.

    Retourne:
        None
    """
    try:
        # Récupération des données via une requête GET avec un timeout de 10s
        response = requests.get(
            'https://jsonplaceholder.typicode.com/posts', timeout=10)

        # Afficher le statut de la requête
        print(f"Status Code: {response.status_code}")

        # Si la requête est réussie, traiter et afficher les titres
        if response.status_code == 200:
            posts = response.json()  # Convertir les données en JSON
            for post in posts:
                print(post['title'])  # Afficher le titre de chaque post
        else:
            print("Échec de la récupération des données.")
    except requests.Timeout:
        print("La requête a expiré.")
    except requests.RequestException as e:
        print(f"Une erreur s'est produite : {e}")


def fetch_and_save_posts():
    """
    Récupère les posts de l'API JSONPlaceholder et les sauvegarde
    dans un fichier CSV.

    Cette fonction utilise la méthode GET pour envoyer une requête HTTP à
    l'API JSONPlaceholder. Si la requête réussit, elle structure les données
    en une liste de dictionnaire contenant les champs 'id', 'title', et 'body',
    puis enregistre ces données dans un fichier CSV nommé 'posts.csv'.

    Si la requête échoue, un message d'erreur est affiché.

    Retourne:
        None
    """
    try:
        # Récupération des données via une requête GET avec un timeout de 10s
        response = requests.get(
            'https://jsonplaceholder.typicode.com/posts', timeout=10)

        # Si la requête est good, traiter et sauvegarder les données dans CSV
        if response.status_code == 200:
            posts = response.json()  # Convertir les données en JSON

            # Structurer les données sous forme de dictionnaires
            data = [{'id': post['id'], 'title': post['title'], 'body': post[
                'body']} for post in posts]

            # Écrire les données dans un fichier CSV
            with open('posts.csv', mode='w', newline='',
                      encoding='utf-8') as file:
                writer = csv.DictWriter(
                    file, fieldnames=['id', 'title', 'body'])
                writer.writeheader()  # Écrire les en-têtes
                writer.writerows(data)  # Écrire les lignes

            print("Les données ont été sauvegardées dans posts.csv.")
        else:
            print("Échec de la récupération des données.")
    except requests.Timeout:
        print("La requête a expiré.")
    except requests.RequestException as e:
        print(f"Une erreur s'est produite : {e}")
