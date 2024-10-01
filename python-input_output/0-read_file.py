#!/usr/bin/python3
"""
Ce script contient une fonction qui lit le contenu d'un fichier et l'affiche
sur la sortie standard.
"""

def read_file(filename=""):
    """
    Lit le contenu d'un fichier et l'affiche sur la sortie standard.

    Args:
        filename (str, optional): Le chemin du fichier à lire.
            Par défaut, une chaîne vide.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
