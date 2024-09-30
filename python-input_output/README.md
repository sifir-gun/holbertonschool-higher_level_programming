# Python - Input/Output

## Description
Ce projet porte sur la gestion de l'entrée et de la sortie (I/O) en Python. Vous apprendrez comment lire et écrire dans des fichiers, gérer les exceptions liées aux fichiers, et travailler avec le format JSON pour la sérialisation et la désérialisation de données. Le projet couvre également l'utilisation des arguments de ligne de commande dans les scripts Python.

## Ressources
Voici les ressources recommandées pour ce projet :
- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3: Chapter 11. Files](http://www.diveintopython3.net/files.html) (jusqu'à "11.4 Binary Files" inclus)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8 : Reading / Writing Files](http://www.freenetpages.co.uk/hp/alan.gauld/tutinput.htm)
- [Automate the Boring Stuff with Python (ch. 8 et ch. 14)](https://automatetheboringstuff.com/)

## Objectifs d'apprentissage
À la fin de ce projet, vous devriez être capable de :
- Comprendre pourquoi la programmation en Python est impressionnante.
- Ouvrir un fichier et lire son contenu.
- Écrire du texte dans un fichier.
- Lire un fichier ligne par ligne ou en entier.
- Déplacer le curseur dans un fichier.
- Garantir la fermeture d'un fichier après l'utilisation.
- Utiliser l'instruction `with` pour la gestion de fichiers.
- Travailler avec le format JSON : sérialisation et désérialisation.
- Convertir une structure de données Python en une chaîne JSON.
- Convertir une chaîne JSON en une structure de données Python.
- Accéder aux paramètres de la ligne de commande dans un script Python.

## Exigences du projet
- Tous vos scripts doivent être interprétés/compilés avec Python 3.8.5 sur Ubuntu 20.04 LTS.
- Chaque fichier doit se terminer par une nouvelle ligne.
- La première ligne de tous vos scripts doit être `#!/usr/bin/python3`.
- Votre code doit suivre la norme **pycodestyle** (version 2.7.*).
- Tous vos fichiers doivent être exécutables.

## Tests
- Tous vos fichiers de tests doivent être dans un dossier nommé `tests`.
- Les tests doivent être exécutés avec la commande `python3 -m doctest ./tests/*`.
- Tous vos modules, classes, et fonctions doivent contenir des docstrings.

## Liste des tâches

### 0. Read file
- Écrivez une fonction `read_file(filename="")` qui lit un fichier texte (UTF8) et affiche son contenu à l'écran.
- Utilisez l'instruction `with` et ne gérez pas les exceptions.

### 1. Write to a file
- Écrivez une fonction `write_file(filename="", text="")` qui écrit une chaîne de texte dans un fichier (UTF8) et retourne le nombre de caractères écrits.

### 2. Append to a file
- Écrivez une fonction `append_write(filename="", text="")` qui ajoute une chaîne de texte à la fin d'un fichier (UTF8) et retourne le nombre de caractères ajoutés.

### 3. To JSON string
- Écrivez une fonction `to_json_string(my_obj)` qui retourne la représentation JSON d'un objet (sous forme de chaîne).

### 4. From JSON string to Object
- Écrivez une fonction `from_json_string(my_str)` qui retourne un objet Python représenté par une chaîne JSON.

### 5. Save Object to a file
- Écrivez une fonction `save_to_json_file(my_obj, filename)` qui écrit un objet dans un fichier texte en utilisant la représentation JSON.

### 6. Create object from a JSON file
- Écrivez une fonction `load_from_json_file(filename)` qui crée un objet à partir d'un fichier JSON.

### 7. Load, add, save
- Écrivez un script qui ajoute tous les arguments à une liste Python, puis les enregistre dans un fichier au format JSON. Si le fichier n'existe pas, il doit être créé.

### 8. Class to JSON
- Écrivez une fonction `class_to_json(obj)` qui retourne le dictionnaire avec des structures de données simples pour la sérialisation JSON d'un objet.

### 9. Student to JSON
- Créez une classe `Student` qui définit un étudiant avec les attributs `first_name`, `last_name`, et `age`. Ajoutez une méthode `to_json()` qui récupère une représentation sous forme de dictionnaire d'une instance de `Student`.

### 10. Student to JSON with filter
- Modifiez la classe `Student` pour ajouter une méthode `to_json(self, attrs=None)` qui récupère une représentation du dictionnaire en fonction de certains attributs spécifiés.

### 11. Student to disk and reload
- Ajoutez une méthode `reload_from_json(self, json)` qui remplace tous les attributs d'une instance `Student` à partir d'un dictionnaire JSON.

### 12. Pascal's Triangle
- Écrivez une fonction `pascal_triangle(n)` qui retourne une liste de listes représentant le triangle de Pascal pour `n`.

## Référentiel GitHub
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-input_output`
