import socket 
import threading 

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
FORMAT = ('utf-8')
clients, names = [], []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def startServer():
    print(f"Server has started on....[Listening][{HOST}]")
    
    server.listen()
    
    while True:
        conn, addr = server.accept()
        conn.send('NAME'.encode(FORMAT))
        
        name = conn.recv(1024).decode(FORMAT)
        
        clients.append(conn)
        names.append(addr)
        print(f'Name : {name}')
        
        broadcastMessage(f'{name} has joined the server!'.encode(FORMAT))
        conn.send(f"[Connected...]".encode(FORMAT))
        
        thread = threading.Thread(target=handle, args=(conn, addr))
        thread.start()
        print(f'[Active connection....] [{threading.active_count() - 1}]')

def handle(conn, addr):
    print(f'[New Connection...] {addr}')
    
    connected = True
    while connected:
        message = conn.recv(1024)
        broadcastMessage(message)
    conn.close()
    

def broadcastMessage(message):
    for client in clients:
        client.send(message)


startServer()