import threading

class Hello(threading.Thread):
    """print hello in a thread"""
    # subclasses of Thread should define a run() function
    def run(self):
        """print hello"""
        print 'hello'

class Goodbye(threading.Thread):
    """print hello in a thread"""
    # subclasses of Thread should define a run() function
    def run(self):
        """print goodbye"""
        for c in "hellodolly": print c 



def beatles():
    """print hello goodbye"""
    hello = Hello()
    goodbye = Goodbye()
    hello.start()
    goodbye.start()
    for x in range(10): print '*'
    
