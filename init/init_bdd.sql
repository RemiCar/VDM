-- Creation de la database si elle n'existe pas
CREATE DATABASE IF NOT EXISTS vdm;

-- Creation d'un user
CREATE USER IF NOT EXISTS 'user_vdm'@'localhost' IDENTIFIED BY '0000';
GRANT ALL PRIVILEGES ON vmd.* TO 'user_vdm'@'localhost';

-- Suppression des tables si elles existent
DROP TABLE IF EXISTS `machines`;
DROP TABLE IF EXISTS `users`;

-- Creation des tables
CREATE TABLE `users` (
    `id` int NOT NULL,
    `nom` TEXT UNIQUE,
    PRIMARY KEY (`id`)
);
CREATE TABLE `machines` (
    `id` int NOT NULL,
    `nom` TEXT UNIQUE,
    `ip` TEXT,
    `etat` TEXT,
    'espace_total' TEXT,
    'espace_disponible' TEXT,
    `owner_id` int NOT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT FOREIGN KEY (`owner_id`) REFERENCES `users` (`id`)
);

