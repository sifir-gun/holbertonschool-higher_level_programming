Voici le contenu du fichier README.md pour le projet JavaScript DOM Manipulation :

# JavaScript DOM Manipulation

## Description
Ce projet se concentre sur la manipulation du DOM en utilisant JavaScript. Il explore les concepts de sélection, modification et mise à jour des éléments HTML, ainsi que les interactions avec des APIs pour obtenir et afficher des données.

## Ressources
### À lire ou regarder :
- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [Document Interface](https://developer.mozilla.org/en-US/docs/Web/API/Document)
- [Element Class](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [Locating DOM elements using selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors)
- [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
- [CSS Diner - Play with Selectors](https://flukeout.github.io/)
- [Client-side Web APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs)
- [Introduction to web APIs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
- [Manipulating documents](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
- [Fetching data from the server](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)

## Objectifs d'apprentissage
À la fin de ce projet, vous serez capable de :

### Général
- Sélectionner des éléments HTML en JavaScript.
- Différencier les sélecteurs par ID, classe et nom de balise.
- Modifier le style d'un élément HTML.
- Obtenir et mettre à jour le contenu d'un élément HTML.
- Modifier le DOM.
- Faire des requêtes avec `XmlHTTPRequest`.
- Faire des requêtes avec l'API Fetch.
- Écouter et lier des événements DOM.
- Écouter et lier des événements utilisateurs.

## Exigences
- **Éditeurs autorisés** : tous.
- Tous les fichiers doivent être interprétés dans un navigateur Chrome (version 57.0 ou supérieure).
- Tous les fichiers doivent se terminer par une nouvelle ligne.
- Un fichier `README.md` significatif doit être présent dans le dossier racine du projet.
- Votre code doit respecter les standards **semistandard**.
- L'utilisation de `var` est interdite.
- La page HTML ne doit pas être rechargée pour chaque action (manipulation du DOM, mise à jour de valeurs, récupération de données, etc.).

## Contenu du projet
### Fichiers principaux :
1. `0-script.js` - Mise à jour de la couleur du texte de l'élément `header` en rouge (#FF0000).
2. `1-script.js` - Mise à jour de la couleur du texte de l'élément `header` lors d'un clic sur un élément avec l'ID `red_header`.
3. `2-script.js` - Ajout de la classe CSS `red` à l'élément `header` lors d'un clic sur un élément avec l'ID `red_header`.
4. `3-script.js` - Alternance entre les classes CSS `red` et `green` pour l'élément `header` en fonction des clics sur un élément avec l'ID `toggle_header`.
5. `4-script.js` - Ajout d'un élément `<li>` à une liste HTML lorsque l'utilisateur clique sur un élément avec l'ID `add_item`.
6. `5-script.js` - Mise à jour du texte de l'élément `header` en "New Header!!!" lors d'un clic sur un élément avec l'ID `update_header`.
7. `6-script.js` - Affichage du nom d'un personnage Star Wars obtenu via l'API SWAPI.
8. `7-script.js` - Liste des titres de tous les films Star Wars obtenus via l'API SWAPI.
9. `8-script.js` - Affichage de la traduction de "hello" via une API avec un paramètre de langue.

## Structure du projet

javascript-dom_manipulation/
├── 0-script.js
├── 1-script.js
├── 2-script.js
├── 3-script.js
├── 4-script.js
├── 5-script.js
├── 6-script.js
├── 7-script.js
├── 8-script.js
└── README.md
