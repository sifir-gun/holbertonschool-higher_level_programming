def replace_in_list(my_list, idx, element):
    # Si l'index est trop petit ou trop grand, on ne change rien et on retourne la liste telle quelle
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    # Sinon, on remplace l'élément à la position donnée par le nouvel élément
    my_list[idx] = element
    return my_list
