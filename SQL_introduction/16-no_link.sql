-- Liste tous les enregistrements de 'second_table' où 'name' n'est pas NULL ou vide
-- Affiche le 'score' et le 'name', triés par 'score' de manière décroissante
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
