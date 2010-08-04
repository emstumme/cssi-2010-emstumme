import random
import server

def run_guess_server(port):
    "run guessing game server on the port"""
    server.run_server(port, Server)

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

