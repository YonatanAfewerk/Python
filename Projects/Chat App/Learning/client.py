<<<<<<< HEAD
# import all the required modules
import socket
import threading
from tkinter import *
from tkinter import font
from tkinter import ttk


PORT = 5050
SERVER = "192.168.1.103"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
	
# Create a new client socket
# and connect to the server
client = socket.socket(socket.AF_INET,
					socket.SOCK_STREAM)
client.connect(ADDRESS)
=======
# import all the required modules
import socket as soc
import threading
from tkinter import *
from tkinter import font
from tkinter import ttk

HEADER = 64
PORT = 5050
SERVER = "192.168.1.103"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"
	
DISCONNECT_MESSAGE = '!DISCONNECTED'
ADDR = (SERVER, PORT)

client = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    
    
    print(client.recv(1024).decode(FORMAT)) # receiving message form the server (just added large number so it can be enough to receive)
    

text = input()
send(text)
send(DISCONNECT_MESSAGE) # to stop the connection
	
>>>>>>> 8c662f6f97e0d64e5265aea18fd90c4cf7969d3d
