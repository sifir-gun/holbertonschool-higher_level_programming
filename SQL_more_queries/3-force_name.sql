-- Crée la table 'force_name' avec les colonnes 'id' et 'name'
-- Le champ 'name' ne peut pas être NULL
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
