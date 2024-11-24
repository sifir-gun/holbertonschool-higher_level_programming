// URL de l'API
const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

// Exécuter le script une fois que le DOM est entièrement chargé
document.addEventListener('DOMContentLoaded', function () {
  // Sélectionner l'élément avec l'ID "hello"
  const helloDiv = document.querySelector('#hello');

  // Récupérer les données avec Fetch API
  fetch(apiUrl)
    .then(response => response.json()) // Convertir la réponse en JSON
    .then(data => {
      // Afficher la traduction dans le <div id="hello">
      helloDiv.textContent = data.hello;
    })
    .catch(error => {
      // Gérer les erreurs éventuelles
      console.error('Erreur lors de la récupération des données :', error);
    });
});
