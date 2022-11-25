#!/usr/bin/python3

import core_script as cs
import os
import subprocess


def ping(address):
    response=subprocess.run(["ping","-c","1","-w","1",address], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode
    if response == 0:
        return '<p style="color:rgb(0,100,0)">UP</p>'
    else:
        return '<p style="color:rgb(255,0,0)">DOWN</p>'


res =  cs.cgi_connect('liste_all')
all_machines = [list(m) for m in res]

for machine in all_machines:
    machine.append(ping(machine[1]))

    
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
            <li>""" + machine[0] + """ | """ + machine[3] + """ | """ + machine[2] + """ </li>"""
html+="""
        </ul>
        <br>"""


### FOOTER HTML
html+="""        
    </body>
</html>"""
print(html)
