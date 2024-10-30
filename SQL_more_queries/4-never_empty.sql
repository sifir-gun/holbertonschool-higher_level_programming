-- Crée la table 'id_not_null' avec les colonnes 'id' et 'name'
-- La colonne 'id' a une valeur par défaut de 1 et ne peut pas être NULL
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
