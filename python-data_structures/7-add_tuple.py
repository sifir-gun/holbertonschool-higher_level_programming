#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Assigner une valeur par déf de 0 pour les éléments manquants dans tuple_a
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    
    # Assigner une valeur par déf de 0 pour les éléments manquants dans tuple_b
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    
    # Additionner les premiers éléments et les deuxièmes éléments
    return (a1 + b1, a2 + b2)
