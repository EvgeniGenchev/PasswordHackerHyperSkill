import sys
import socket

inputs = sys.argv

address = inputs[1]
port = int(inputs[2])
message = inputs[3]

with socket.socket() as soc:
    soc.connect((address, port))
    soc.send(message.encode())
    print(soc.recv(1024).decode())

