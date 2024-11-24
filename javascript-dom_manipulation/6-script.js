// URL de l'API
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Sélectionner l'élément avec l'ID "character"
const characterDiv = document.querySelector('#character');

// Récupérer les données avec Fetch API
fetch(apiUrl)
  .then(response => response.json()) // Convertir la réponse en JSON
  .then(data => {
    // Afficher le nom du personnage dans l'élément <div id="character">
    characterDiv.textContent = data.name;
  })
  .catch(error => {
    // Gérer les erreurs éventuelles
    console.error('Erreur lors de la récupération des données :', error);
  });
  