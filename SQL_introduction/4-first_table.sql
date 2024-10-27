-- Crée la table 'first_table' avec les colonnes 'id' et 'name' si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
