// Sélectionner l'élément avec l'ID "update_header"
const updateHeader = document.querySelector('#update_header');

// Sélectionner l'élément <header>
const header = document.querySelector('header');

// Ajouter un écouteur d'événements au clic
updateHeader.addEventListener('click', function () {
  // Mettre à jour le texte de <header>
  header.textContent = 'New Header!!!';
});
