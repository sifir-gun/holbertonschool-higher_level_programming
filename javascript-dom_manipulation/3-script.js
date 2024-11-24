// Sélectionner l'élément avec l'ID "toggle_header"
const toggleHeader = document.querySelector('#toggle_header');

// Sélectionner l'élément <header>
const header = document.querySelector('header');

// Ajouter un écouteur d'événements au clic
toggleHeader.addEventListener('click', function () {
  // Alterner entre les classes "red" et "green"
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
