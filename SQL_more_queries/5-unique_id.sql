-- Crée la table 'unique_id' avec les colonnes 'id' et 'name'
-- La colonne 'id' a une valeur par défaut de 1, doit être unique et ne peut pas être NULL
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
