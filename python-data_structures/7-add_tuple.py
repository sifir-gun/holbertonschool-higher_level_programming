#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Compléter les tuples avec des zéros si nécessaire
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Ajouter les premiers éléments et les deuxièmes éléments
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
