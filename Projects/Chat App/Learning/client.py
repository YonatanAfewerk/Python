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
