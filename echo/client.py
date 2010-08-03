# client.py

import socket

def client(host, port):
    """connect the client to host:port"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port)) # connect client to host:port
    print 'connected to' , (host,port)
    while True:
        message = raw_input('?')
        if not message:
            break
        s.send(message) # send info to server
        data = s.recv(1024)# read info from the server
        print 'recv:', data #print what we got back
        if data == "you won":
            break
    s.close #close socket
