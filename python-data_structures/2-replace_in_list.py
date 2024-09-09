def replace_in_list(my_list, idx, element):
    # Vérifie si l'indice est valide
    if idx < 0 or idx >= len(my_list):
        return my_list  # Retourne la liste originale si l'indice est invalide
    
    # Copie la liste pour ne pas modifier l'originale
    new_list = my_list.copy()
    new_list[idx] = element  # Remplace l'élément à la position donnée
    return new_list  # Retourne la nouvelle liste
