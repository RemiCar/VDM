#!/bin/python

import socket

HOST = "127.0.0.1"
PORT = 45679

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    close = False
    while not close:
        msg = input(">$ ")
        if msg == 'quit':
            close = True
        s.sendall(msg.encode())
        data = s.recv(1024)
        if data:
            print(f"{data.decode()}")
    

