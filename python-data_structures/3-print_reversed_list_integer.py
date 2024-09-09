def print_reversed_list_integer(my_list=[]):
    if my_list:  # Vérifie si la liste n'est pas vide
        for i in reversed(my_list):  # Parcourt la liste dans l'ordre inverse
            print("{:d}".format(i))  # Affiche chaque entier avec str.format()
