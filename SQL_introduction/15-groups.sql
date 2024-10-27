-- Liste le nombre d'enregistrements pour chaque score dans 'second_table'
-- Affiche le 'score' et le nombre d'enregistrements pour ce score sous le nom 'number'
-- Trie la liste par le nombre d'enregistrements de manière décroissante
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
