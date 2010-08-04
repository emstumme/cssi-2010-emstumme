# client.py

import socket
import sys 

#client
#
#start up stuff
# while True:
#   processing on response
#   possible quit
#   send request to server
#   recieve response form server
# finish up stuff

class Client(object):
    """guessing game client class"""

    def startup(self):
        """startup guessing game client"""
        self.playing = True
        self.num_guesses = 0 
        print ' guess a number between 1 and a 100'

    def running(self):
        """return true if we are running"""
        return self.playing

    def process(self, data):
        """process data and return server request data is initially none"""
        if not data is None:
            print data
            if data == "you won":
                self.playing = False
                return
        guess = raw_input('your guess ?')
        self.num_guesses += 1 
        return guess

    def finish(self):
        "finish the client guessing game"""
        print ('you used ' + str(self.num_guesses) + 'guesses')



def run_client(host, port):
    """connect the client to host:port"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port)) # connect client to host:port
    client = Client()
    client.startup()
    data = None
    while True:
        request = client.process(data)
        if not client.running():
            break
        s.send(request) # send info to server
        data = s.recv(1024)# read info from the server
    client.finish()
    s.close #close socket

if __name__ == "__main__":
    # should be run as: python guess_server.py <port>
    host = None
    port = None
    try:
        host = sys.argv[1]  # host argument
        port = int(sys.argv[2]) # get port argument
    except:
        print 'usage:', sys.argv[0], '<host> <port>'
    if host and port:
        run_client(host, port)
    
