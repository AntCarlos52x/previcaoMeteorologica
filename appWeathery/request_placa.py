import socket
from time import sleep

SERVER_IP = "192.168.0.100"
PORT = 80

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))
        s.sendall(command.encode())
        print(f"Comando enviado: {command}")