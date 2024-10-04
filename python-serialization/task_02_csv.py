"""
Ce module fournit une fonction pour convertir les données d'un fichier CSV
en un fichier JSON en utilisant les techniques de sérialisation.

Fonctions :
- convert_csv_to_json(csv_filename) :
Convertit les données d'un fichier CSV en JSON.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convertit les données d'un fichier CSV en un fichier JSON.

    Args:
        csv_filename (str): Le nom du fichier CSV à convertir.

    Returns:
        bool: True si la conversion a réussi, False sinon.
    """
    try:
        # Ouvre le fichier CSV et lit les données avec DictReader
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # Convertit chaque ligne en un dictionnaire
            data = list(csv_reader)

        # Sérialise la liste des dictionnaires dans un fichier JSON
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        print(f"Le fichier {csv_filename} est introuvable.")
        return False
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return False
