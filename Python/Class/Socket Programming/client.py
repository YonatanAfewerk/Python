import socket as soc
# from requests import get

HEADER = 64
PORT = 5050
# SERVER = get("https://api.ipify.org").text
SERVER = '192.168.1.103'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECTED'
ADDR = (SERVER, PORT)

client = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
    
    print(client.recv(5050).decode(FORMAT)) # receiving message form the server (just added large number so it can be enough to receive)
    

text = input()
send(text)
send(DISCONNECT_MESSAGE) # to stop the connection