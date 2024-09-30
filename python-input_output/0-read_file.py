#!/usr/bin/python3
def read_file(filename=""):
    """
    Lit le contenu d'un fichier et l'affiche sur la sortie standard.

    Args:
        filename (str): Le chemin du fichier à lire.
        Par défaut, une chaîne vide.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
