-- Liste tous les shows avec leur genre associé, ou NULL si aucun genre n'est associé
-- Affiche 'tv_shows.title' et 'tv_show_genres.genre_id'
-- Trie les résultats par 'tv_shows.title' puis par 'tv_show_genres.genre_id'
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
