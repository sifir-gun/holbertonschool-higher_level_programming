// Sélectionner l'élément avec l'ID "add_item"
const addItem = document.querySelector('#add_item');

// Sélectionner la liste avec la classe "my_list"
const myList = document.querySelector('.my_list');

// Ajouter un écouteur d'événements au clic
addItem.addEventListener('click', function () {
  // Créer un nouvel élément <li>
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';

  // Ajouter le nouvel élément à la liste
  myList.appendChild(newItem);
});
