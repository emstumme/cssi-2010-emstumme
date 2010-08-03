# server.py - run our web service

import socket # contains low-level network functions

def server(port):
    """run our server on the given port"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        host = '' # all available netwrok interfaces
        s.bind((host, port)) # (host,port) <=> host:port
        s.listen(True) # listen for incoming connection
        conn, addr = s.accept() # accept a connection
        print 'connection recieved from:', addr
        #now we have our connection, we can do something

        # read data from the connection
        # this is like raw_input()
        data = conn.recv(1024) # recv is like "read"
        conn.send(data) # send sends data back to the client
        conn.close()
        s.close()
    except:
        print 'There was an error'
        s.close()
    
    
