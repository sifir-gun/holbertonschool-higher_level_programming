-- Crée la base de données 'hbtn_0d_usa' si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utilise la base de données 'hbtn_0d_usa'
USE hbtn_0d_usa;

-- Crée la table 'cities' avec les colonnes 'id', 'state_id' et 'name'
-- La colonne 'id' est un entier auto-incrémenté, clé primaire et unique
-- La colonne 'state_id' est un entier non nul et une clé étrangère vers 'id' de la table 'states'
-- La colonne 'name' est un champ VARCHAR de 256 caractères qui ne peut pas être NULL
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
