-- Crée la base de données 'hbtn_0d_2' si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Crée l'utilisateur 'user_0d_2' avec le mot de passe 'user_0d_2_pwd' s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Donne le privilège SELECT uniquement sur la base de données 'hbtn_0d_2' à 'user_0d_2'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Applique les modifications de privilèges
FLUSH PRIVILEGES;
