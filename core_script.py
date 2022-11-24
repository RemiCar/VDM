#!/bin/python

import sys
import mariadb

def add(cur, *arg):
    ### Ajoute une nouvelle machine (nom, ip, user)
    # Verification argument
    if len(arg) != 3:
        print("Arguments incorrect")
        exit()
    nom, ip, user = arg[0], arg[1], arg[2]
    # A partir du nom du user, on doit recuperer son id dans la table Users
    user_id = get_userid(cur,user)[0][0]
    request="""
        INSERT INTO Machine (Nom, IP, Owner_id) VALUES 
            (?,?,?)
    ;"""
    try:
        cur.execute(request,[nom,ip,user_id])
    except:
        print("Impossible d'ajouter la nouvelle entrée")

def get_userid(cur,*arg):
    ### Retourne l'id d'un user 'nom_user'
    # Verification argument
    if len(arg) != 1:
        print("Arguments incorrect")
        exit()
    nom_user = arg[0]
    request="""
        SELECT User_id FROM Users
        WHERE Nom_user = ?
    ;"""
    cur.execute(request,[nom_user])
    return [l for l in cur]

def remove(cur, *arg):
    ### Supprime une machine 'nom'
    # Verification argument
    if len(arg) != 1:
        print("Arguments incorrect")
        exit()
    nom = arg[0]
    request="""
        DELETE FROM Machine
        WHERE Nom = ?
    ;"""
    try:
        cur.execute(request,[nom])
    except:
        print("Impossible de supprimer l'entrée")

def change(cur, *arg):
    ### Change le nom du machine (old) par un nouveau (new)
    # Verification argument
    if len(arg) != 2:
        print("Arguments incorrect")
        exit()
    old, new = arg[0], arg[1]
    request="""
        UPDATE Machine
        SET Nom = ?
        WHERE Nom = ?
    ;"""
    try:
        cur.execute(request,[new,old])
    except:
        print("Impossible de modifier l'entrée")

def liste_all(cur):
    ### Liste toutes les machines de tout les users
    request="""
        SELECT Machine.Nom, Machine.IP, Users.Nom_user FROM Machine
        INNER JOIN Users ON Machine.owner_id=Users.User_id
    ;"""
    cur.execute(request)
    return [l for l in cur]

def liste(cur, *arg):
    ### Liste les machines d'un user 'nom'
    # Verification argument
    if len(arg) != 1:
        print("Arguments incorrect")
        exit()
    nom = arg[0]
    request="""
        SELECT Machine.Nom, Machine.IP FROM Machine 
        INNER JOIN Users ON Machine.owner_id=Users.User_id 
        WHERE Users.Nom_user = ?
    ;"""
    cur.execute(request,[nom])
    return [l for l in cur]



argv= sys.argv[1:]

_fonction = {'add' : add,'remove' : remove, 'change': change, 'liste': liste, 'liste_all' : liste_all}

if argv[0] not in _fonction:
    print("Erreur: option invalide")
    exit()

try:
    conn = mariadb.connect(user="user_vdm",password="0000",host="localhost",port=3306, database="VDM")
except mariadb.Error as e:
    print(f"Erreur de connexion à la bdd: {e}")
    exit()

cur = conn.cursor()
res = _fonction[argv[0]](cur,*argv[1:])
conn.commit()
conn.close()