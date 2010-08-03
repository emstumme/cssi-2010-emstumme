# server.py - run our web service

import socket # contains low-level network functions

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
#final stuff

import random 

class Server(object):
    """guessing game server"""

    def startup(self):
        """start a guessing game"""
        self.x = random.randint(1,100)
        self.num_guesses = 0
        print '(our number is' + str(self.x) +')'

    def process(self,data):
        """process user input for guessing game"""
        guess = int(data)
        self.num_guesses += 1
        if guess == self.x:
            return "you won"
        elif guess > self.x:
            return "too high"
        else:
            return "too low"

    def finish(self):
        "finish up the guessing game"""
        print 'user used' + str(self.num_guesses) + 'guesses'

def handle_connection(conn, addr):
    print 'connection recieved from:', addr
    server = Server()
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

def run_server(port):
    """run our server on the given port"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '' # all available netwrok interfaces
    s.bind((host, port)) # (host,port) <=> host:port
    s.listen(True) # listen for incoming connection
    print 'listening on port', port
    while True:
        conn, addr = s.accept() # accept a connection
        handle_connection(conn, addr)
    s.close() # can't ge there because of loop
   
    
    
