#!/bin/python

import core_script as cs
import os


def ping(address):
    response = os.system("ping -c1 -w1 "+address)
    if response == 0:
        return '<p style="color:rgb(0,100,0)">UP</p>'
    else:
        return '<p style="color:rgb(255,0,0)">DOWN</p>'



all_machines =  cs.cgi_connect('liste_all')

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
            <li>""" + machine[0] + """ | """ + ping(machine[1]) + """ | """ + machine[2] + """ </li>"""
html+="""
        </ul>
        <br>"""


### FOOTER HTML
html+="""        
    </body>
</html>"""
print(html)
