#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Tente d'imprimer l'élément en tant qu'entier
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Continue si l'élément ne peut pas être converti en entier
            continue
        except IndexError:
            # Si l'index dépasse la taille de la liste, arrête la boucle
            break
    print("")  # Imprime une nouvelle ligne à la fin
    return count
