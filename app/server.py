# server.py - run our web service

import socket # contains low-level network functions
import threading

# general server processing
#
# what happens when we handle a connection
#
# start up stuff
# while True:
#       read some data from client
#       if no data then we break out of that loop
#       processing on that data
#       send a response to the client
# final stuff

class HandleConnection(threading.Thread):
    def __init__(conn, add, create):
        Thread.__init__(self)
        self.conn = conn
        self.add = add
        self.create = create
    def run(self):
        handle_connection(self.conn, self.addr, self.create)

def handle_connection(conn, addr, create):
    print 'connection recieved from:', addr
    server = create()
    server.startup()
    while True:
        data = conn.recv(1024) # recv is like "read"
        if not data:
            break
        print 'from client:', data
        response = server.process(data)
        conn.send(response)
    server.finish()
    conn.close()

def run_server(port, create):
    """run our server on the given port"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '' # all available netwrok interfaces
    s.bind((host, port)) # (host,port) <=> host:port
    s.listen(True) # listen for incoming connection
    print 'listening on port', port
    while True:
        conn, addr = s.accept() # accept a connection
        new_connection = HandleConnection(conn, addr, create)
        new_conncection.start
        # handle_connection(conn, addr, create)
    s.close() # can't ge there because of loop
   
    
    
