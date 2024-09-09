#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        # Retourner une copie de la liste originale si l'index est invalide
        return my_list[:]
    # Créer une copie de la liste originale
    new_list = my_list[:]
    # Remplacer l'élément à la position donnée dans la copie
    new_list[idx] = element
    return new_list
