-- Crée l'utilisateur 'user_0d_1' avec le mot de passe 'user_0d_1_pwd'
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Donne tous les privilèges à 'user_0d_1' sur toutes les bases de données et tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Applique les modifications de privilèges
FLUSH PRIVILEGES;
