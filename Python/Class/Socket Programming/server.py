import socket as soc
import threading 

HEADER = 64
PORT = 5050
SERVER = '0.0.0.0'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECTED'

socket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
ADDR = (SERVER, PORT)

server = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
server.bind(ADDR)


def handle_Client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # return's the length of the message
        if msg_length: # to check if its not null
            msg_length = int(msg_length) # change that into an int
            msg = conn.recv(msg_length).decode(FORMAT) # and use the converted value as the amount of bytes (we r receiving)  
            
            if msg != DISCONNECT_MESSAGE:
                print(f"[{addr}] {msg}")
                conn.send('sent'.encode(FORMAT))
            else:
                connected = False
                
        
    conn.close()
        

def start():
    server.listen()
    print(f'[LISTENING] server is listening on {SERVER}')
    while True:
        conn, addr = server.accept() # waits for a connection and stores the data in conn, addr
        thread = threading.Thread(target=handle_Client, args=(conn, addr))
        thread.start() # starts the Thread 
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')




print("[STARTING] server is starting ... ")
start()