import socket
import urllib

def listen_callback(port=1111):
    host = '127.0.0.1'  # listen to localhost
    port = port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    while True:
        csock, caddr = sock.accept()
        req = csock.recv(1024)
        if req:
            query_data = urllib.parse.parse_qs(urllib.parse.urlparse(req.decode("utf-8").split("\r\n")[0].split(" ")[1]).query)
            break

    return query_data
