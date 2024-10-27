-- Liste tous les enregistrements de 'second_table' où le score est supérieur ou égal à 10
-- Affiche le 'score' et le 'name', triés par 'score' de manière décroissante
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
