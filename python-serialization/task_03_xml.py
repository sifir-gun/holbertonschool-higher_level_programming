"""
Ce module fournit des fonctions pour sérialiser un dictionnaire Python en XML
et désérialiser un fichier XML en un dictionnaire Python.

Fonctions :
- serialize_to_xml(dictionary, filename) :
Sérialise un dictionnaire Python en XML et le sauvegarde dans un fichier.
- deserialize_from_xml(filename) :
Désérialise un fichier XML en un dictionnaire Python.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python en XML et le sauvegarde dans un fichier.

    Args:
        dictionary (dict): Le dictionnaire Python à sérialiser.
        filename (str):
        Le nom du fichier où les données XML seront sauvegardées.
    """
    # Créer un élément racine nommé 'data'
    root = ET.Element("data")

    # Ajouter les éléments enfants au fichier XML à partir du dictionnaire
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Sauvegarder l'arbre XML dans le fichier spécifié
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML et recrée un dictionnaire Python.

    Args:
        filename (str): Le nom du fichier XML à lire et désérialiser.

    Returns:
        dict: Le dictionnaire Python désérialisé.
    """
    # Charger et analyser l'arbre XML
    tree = ET.parse(filename)
    root = tree.getroot()

    # Recréer le dictionnaire à partir de l'arbre XML
    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
