import socket
import sys
import time
import threading
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1,2]
queue = Queue()
all_connections = []
all_addresses = []

#creating the socket
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 6060
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error",str(msg))  

#binding the socket
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port : ", str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error : "+str(msg)+"\n"+"Retrying...")
        socket_bind()    

#accept connection
def socket_accept():
    conn, address = s.accept()
    print("Connection established,"+"IP"+address[0]+", Port :"+str(address[1]))
    send_commands(conn)
    conn.close()

#send the commands written in the command prompt
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "UTF-8")
            print(client_response, end="")

#Accept connections from multiple clients and save them to the list
def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]    

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()    