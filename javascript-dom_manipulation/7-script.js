// URL de l'API
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Sélectionner l'élément <ul> avec l'ID "list_movies"
const listMovies = document.querySelector('#list_movies');

// Récupérer les données avec Fetch API
fetch(apiUrl)
  .then(response => response.json()) // Convertir la réponse en JSON
  .then(data => {
    // Parcourir les films et ajouter leurs titres à la liste
    data.results.forEach(movie => {
      const listItem = document.createElement('li'); // Créer un <li>
      listItem.textContent = movie.title; // Ajouter le titre du film
      listMovies.appendChild(listItem); // Insérer le <li> dans le <ul>
    });
  })
  .catch(error => {
    // Gérer les erreurs éventuelles
    console.error('Erreur lors de la récupération des données :', error);
  });
  