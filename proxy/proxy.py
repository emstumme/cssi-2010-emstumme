# proxy

import connection
import nameservice
import sys
import socket

def handle_connection(names, conn):
    "connection from a new client"""
    name = conn.recv()
    if not names.add(name, conn):
        print 'name is already in use: ' + name
        conn.send("name is already in use: " + name)
    else:
        print 'name: ' + name + ' added to name service'
        conn.send('name: ' + name)

def run_proxy(port):
    """run our proxy on the given port"""
    host = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(True)
    print 'listening on port', port
    names = nameservice.NameService()
    while True:
        socket_conn, addr = s.accept()
        print 'accept', addr
        conn = connection.Connection(socket_conn)
        handle_connection(names, conn)
    s.close()

if __name__ == "__main__":
    port = int(sys.argv[1])
    run_proxy(port)
