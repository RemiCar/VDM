#!/usr/bin/python3

import core_script as cs
import os
import subprocess


def ping(address):
    #response = os.system("ping -c1 -w1 "+address+" &>/dev/null"
    #process=subprocess.Popen("ping -c1 -w1 "+address+" &>/dev/null", shell=True, stdout=subprocess.PIPE)
    response=subprocess.run(["ping","-c","1","-w","1",address], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode
    #process.wait()
    #response = process.returncode
    print()
    if response == 0:
        return '<p style="color:rgb(0,100,0)">UP</p>'
    else:
        return '<p style="color:rgb(255,0,0)">DOWN</p>'



res =  cs.cgi_connect('liste_all')
all_machines = [list(m) for m in res]



### HEADER HTML
html="""Content-type: text/html

<!DOCTYPE html>
<html>
    <head>
        <title>Page d'accueil</title>
    </head>
    <body>
        """
print(html)
for machine in all_machines:
    machine.append(ping(machine[1]))
### BODY HTML
html="""
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
