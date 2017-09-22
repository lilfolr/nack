import socket
from application import Application
from modules.Discovery.ports import PortScanner

application = Application('google.com')
PS = PortScanner(application)
open_ports = PS.scan(from_port=79, to_port=444, extra_ports=[989, 990])
print ("Open ports = "+str(open_ports))
