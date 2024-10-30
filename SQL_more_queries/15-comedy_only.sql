-- Liste tous les shows de genre 'Comedy'
-- Affiche uniquement la colonne 'title' de 'tv_shows' en triant par ordre alphabétique
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
