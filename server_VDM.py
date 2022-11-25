#!/bin/python

import socket
import os


def menu(cmd):
    match cmd:
        case 'quit':
            return "Déconnexion"
        case 'ls':
            return str(os.listdir())
        case _:
            print(f"reçu {cmd}")
            return 'Commande Inconnue'








if __name__=="__main__":

    HOST = "127.0.0.1"
    PORT = 45678

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))

        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connection de {addr}")
                close = False
                while not close:
                    data = conn.recv(1024)
                    if not data:
                        close = True
                    else:
                        to_send = menu(data.decode())
                        conn.sendall(to_send.encode())
                print(f"Deconnexion de {addr}")