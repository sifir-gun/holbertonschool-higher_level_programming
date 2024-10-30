-- Liste tous les shows avec leurs genres, affiche NULL si aucun genre n'est associé
-- Affiche 'tv_shows.title' et 'tv_genres.name' en triant par 'tv_shows.title' et 'tv_genres.name'
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
