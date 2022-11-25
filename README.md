# VDM

## Utilisation via SSH

### Installation

#### NGINX
Créer un utilisateur VDM_user
Mettre la conf nginx/serverhttps.fr.conf dans le dossier /etc/nginx/sites-available et le lien symbolique dans sites-enabled et redemarrer nginx.
Changer la conf du service fcgiwrap en changeant l'user en VDM_user
Démarrer fcgi


Changer le owner de core_script.py pour VDM_user
Donner les droits d'execution
Ajouter un lien symbolique de core_script.py à /usr/bin/
Le rajouter à la variable $PATH

Installer le module mariadb
Faire la configuration de mariadb et créer un user
Récupérer le contenu de la bdd dans le fichier VDM.sql
Lancer mariadb

### Utilisation

#### ajouter une machine
core_script.py add <nom-machine> <address-ip> <nom_user>

#### modifier le nom d'une machine
core_script.py change <nom-machine-cible> <nouveau-nom-machine>

#### supprimer une machine
core_script.py remove <nom-machine>

#### afficher les machines d'un utilisateur
core_script.py liste <nom_user>

#### afficher toutes les machines
core_script.py liste_all


## Utilisation via CGI

### Installation

Le core_script.py doit être dans le même dossier que index.py
