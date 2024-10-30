-- Liste tous les genres et le nombre de shows associés
-- Affiche les colonnes 'genre' et 'number_of_shows' en triant par 'number_of_shows' décroissant
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
