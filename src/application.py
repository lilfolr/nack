import socket

class Application(object):
    def __init__(self, host):
        self.ip = socket.gethostbyname(host)
