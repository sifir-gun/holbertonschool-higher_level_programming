-- Liste toutes les villes de Californie en utilisant une sous-requête pour obtenir l'identifiant de l'état 'California'
-- Trie les résultats par l'identifiant de la ville de manière croissante
SELECT id, name 
FROM cities 
WHERE state_id = (
    SELECT id 
    FROM states 
    WHERE name = 'California'
)
ORDER BY id ASC;
