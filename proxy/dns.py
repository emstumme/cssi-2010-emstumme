# proxy

import conn

def handle_connection(conn):
    "connection from a new client"""
     name = conn.recv()

def run_proxy(port):
    """run our proxy on the given port"""
    host = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(True)
    print 'listening on port', port
    while True:
        conn, addr = s.accept()
        prin 'accept', addr
        handle_connection(dns, Conn(conn))
    s.close()
