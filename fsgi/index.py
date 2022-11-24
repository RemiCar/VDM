#!/bin/python

import main_script as ms
import os


def ping(address):
    response = os.system("ping -c1 -w1 "+address)
    if response == 0:
        return '<p style="color:rgb(0,100,0)">UP</p>'
    else:
        return '<p style="color:rgb(255,0,0)">DOWN</p>'





all_machines = ms.sel_all() # Fonction de main_script qui "SELECT machines.nom, machines.ip, users.nom FROM machines INNER JOIN users ON ..."


### HEADER HTML
html="""Content-type: text/html

<!DOCTYPE html>
<html>
    <head>
        <title>Page d'accueil</title>
    </head>
    <body>
        """


### BODY HTML
html+="""
        <ul>"""
for machine in all_machines:
    html+="""
            <li>""" + all_machines[0] + """ | """ + ping(all_machines[1]) + """ | """ + all_machines[2] + """ </li>"""
html+="""
        </ul>
        <br>"""


### FOOTER HTML
html+="""        
    </body>
</html>"""
print(html)
