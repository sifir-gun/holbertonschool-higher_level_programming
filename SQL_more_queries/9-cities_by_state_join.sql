-- Liste toutes les villes et leurs états associés
-- Affiche 'cities.id', 'cities.name' et 'states.name' en triant par 'cities.id' de manière croissante
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
