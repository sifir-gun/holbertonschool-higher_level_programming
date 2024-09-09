# Python Data Structures: Lists and Tuples

## Description
Ce projet est axé sur l'apprentissage et l'utilisation des structures de données telles que les listes et les tuples en Python. À la fin de ce projet, vous serez capable d'expliquer et d'utiliser efficacement ces structures dans vos programmes Python.

## Resources
### Lecture
- [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html) (jusqu'à la section 5.3 incluse)
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

## Learning Objectives
À la fin de ce projet, vous serez capable d'expliquer, sans aide extérieure, les concepts suivants :

### Général
- Qu'est-ce qu'une liste et comment l'utiliser ?
- Quelles sont les différences et similitudes entre les chaînes de caractères et les listes ?
- Quelles sont les méthodes les plus courantes pour manipuler les listes et comment les utiliser ?
- Comment utiliser les listes comme piles et files d'attente ?
- Qu'est-ce que les compréhensions de liste et comment les utiliser ?
- Qu'est-ce qu'un tuple et comment l'utiliser ?
- Quand utiliser un tuple par rapport à une liste ?
- Qu'est-ce qu'une séquence ?
- Qu'est-ce que le « tuple packing » et « sequence unpacking » ?
- Qu'est-ce que l'instruction `del` et comment l'utiliser ?

## Requirements
### Python Scripts
- Éditeurs autorisés : `vi`, `vim`, `emacs`
- Tous vos fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS en utilisant `python3` (version 3.8.5)
- Tous vos fichiers doivent se terminer par une nouvelle ligne
- La première ligne de tous vos fichiers doit être `#!/usr/bin/python3`
- Un fichier `README.md` à la racine du projet est obligatoire
- Votre code doit respecter le style PEP8 (version 2.7.*)
- Tous vos fichiers doivent être exécutables
- La longueur de vos fichiers sera vérifiée avec `wc`

## Tasks

### 0. Print a list of integers
Écrire une fonction qui affiche tous les entiers d'une liste.  
Prototype : `def print_list_integer(my_list=[])`  
Vous devez utiliser `str.format()` pour afficher les entiers.

### 1. Secure access to an element in a list
Écrire une fonction qui récupère un élément à une position donnée dans une liste.  
Prototype : `def element_at(my_list, idx)`

### 2. Replace element
Écrire une fonction qui remplace un élément d'une liste à une position spécifique.  
Prototype : `def replace_in_list(my_list, idx, element)`

### 3. Print a list of integers... in reverse!
Écrire une fonction qui affiche tous les entiers d'une liste dans l'ordre inverse.  
Prototype : `def print_reversed_list_integer(my_list=[])`

### 4. Replace in a copy
Écrire une fonction qui remplace un élément d'une liste à une position spécifique sans modifier la liste d'origine.  
Prototype : `def new_in_list(my_list, idx, element)`

### 5. Can you C me now?
Écrire une fonction qui supprime tous les caractères `c` et `C` d'une chaîne.  
Prototype : `def no_c(my_string)`

### 6. Lists of lists = Matrix
Écrire une fonction qui affiche une matrice d'entiers.  
Prototype : `def print_matrix_integer(matrix=[[]])`

### 7. Tuples addition
Écrire une fonction qui additionne deux tuples.  
Prototype : `def add_tuple(tuple_a=(), tuple_b=())`

### 8. More returns!
Écrire une fonction qui retourne un tuple contenant la longueur d'une chaîne et son premier caractère.  
Prototype : `def multiple_returns(sentence)`

### 9. Find the max
Écrire une fonction qui trouve le plus grand entier d'une liste.  
Prototype : `def max_integer(my_list=[])`

### 10. Only by 2
Écrire une fonction qui trouve tous les multiples de 2 dans une liste.  
Prototype : `def divisible_by_2(my_list=[])`

### 11. Delete at
Écrire une fonction qui supprime l'élément à une position spécifique dans une liste.  
Prototype : `def delete_at(my_list=[], idx=0)`

### 12. Switch
Compléter le code source pour intervertir la valeur des variables `a` et `b`.  
Votre programme doit faire exactement 5 lignes.

## Repo
- **Dépôt GitHub :** `holbertonschool-higher_level_programming`
- **Dossier :** `python-data_structures`