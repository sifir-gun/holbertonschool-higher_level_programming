-- Liste tous les shows avec au moins un genre associé
-- Affiche 'tv_shows.title' et 'tv_show_genres.genre_id'
-- Trie les résultats par 'tv_shows.title' puis par 'tv_show_genres.genre_id'
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
