-- Liste tous les shows sans genre associé
-- Affiche 'tv_shows.title' et 'tv_show_genres.genre_id' en triant par 'tv_shows.title' et 'tv_show_genres.genre_id'
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
