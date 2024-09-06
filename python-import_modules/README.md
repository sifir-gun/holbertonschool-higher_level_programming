# Python - Import Modules and Command Line Arguments

## Description

Ce projet a pour but de vous familiariser avec l'importation de fonctions, l'utilisation des arguments en ligne de commande, et la gestion des modules en Python.

### Ressources

- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command Line Arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
- [Pycodestyle – Style Guide for Python Code](https://pycodestyle.pycqa.org/en/latest/)

### Commandes utiles :

- `python3`
- `dir()`

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer les points suivants à quelqu'un sans l'aide de Google :

### Général

- Pourquoi la programmation Python est géniale.
- Comment importer des fonctions depuis un autre fichier.
- Comment utiliser les fonctions importées.
- Comment créer un module.
- Comment utiliser la fonction intégrée `dir()`.
- Comment empêcher le code d'un script d'être exécuté lorsqu'il est importé.
- Comment utiliser les arguments en ligne de commande avec vos programmes Python.

## Exigences

- Éditeurs autorisés : `vi`, `vim`, `emacs`.
- Tous vos fichiers seront interprétés/compilés sur Ubuntu 22.04 LTS en utilisant Python 3.10.
- Tous vos fichiers doivent se terminer par une nouvelle ligne.
- La première ligne de tous vos fichiers doit être exactement `#!/usr/bin/python3`.
- Un fichier `README.md` doit être présent à la racine du projet.
- Votre code doit utiliser le style **Pycodestyle** (version 2.7).
- Tous vos fichiers doivent être exécutables.
- La longueur de vos fichiers sera testée avec la commande `wc`.

---

## Tâches

### 0. Importer une simple fonction d'un simple fichier

Écrivez un programme qui importe la fonction `def add(a, b)` depuis le fichier `add_0.py` et imprime le résultat de l'addition `1 + 2 = 3`.

- Vous devez utiliser la fonction `print` avec le formatage de chaîne pour afficher les entiers.
- Vous devez assigner la valeur `1` à une variable appelée `a`, et la valeur `2` à une variable appelée `b`, et utiliser ces deux variables comme arguments en appelant les fonctions `add` et `print`.
- Exemple de fichier : `0-add.py`

### 1. Ma première boîte à outils !

Écrivez un programme qui importe des fonctions depuis le fichier `calculator_1.py`, effectue des calculs mathématiques, et imprime les résultats.

- Définissez `a = 10` et `b = 5`, puis utilisez ces deux variables comme arguments pour appeler les fonctions importées.
- Exemple de fichier : `1-calculation.py`

### 2. Comment rendre un script dynamique !

Écrivez un programme qui imprime le nombre d'arguments et la liste de ces arguments.

- Exemple de fichier : `2-args.py`

### 3. Addition infinie

Écrivez un programme qui imprime le résultat de l'addition de tous les arguments.

- Vous pouvez convertir les arguments en entiers en utilisant `int()`.
- Exemple de fichier : `3-infinite_add.py`

### 4. Qui êtes-vous ?

Écrivez un programme qui imprime tous les noms définis dans le module compilé `hidden_4.pyc`.

- N'imprimez que les noms qui ne commencent pas par `__`.
- Exemple de fichier : `4-hidden_discovery.py`

### 5. Tout peut être importé

Écrivez un programme qui importe la variable `a` depuis le fichier `variable_load_5.py` et imprime sa valeur.

- Exemple de fichier : `5-variable_load.py`

---

## Dépôt GitHub

- **Dépôt GitHub :** `holbertonschool-higher_level_programming`
- **Dossier :** `python-import_modules`