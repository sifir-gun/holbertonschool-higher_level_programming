// Sélectionner l'élément avec l'ID "red_header"
const redHeader = document.querySelector('#red_header');

// Sélectionner l'élément <header>
const header = document.querySelector('header');

// Ajouter un écouteur d'événements au clic
redHeader.addEventListener('click', function () {
  // Changer la couleur du texte de <header> en rouge
  header.style.color = '#FF0000';
});
