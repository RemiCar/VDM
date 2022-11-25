# VDM

## Utilisation via SSH

### Installation

Changer le owner de core_script.py pour VDM_user
Donner les droits d'execution/
Ajouter un lien symbolique de core_script.py à /usr/bin/
Le rajouter à la variable $PATH

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
