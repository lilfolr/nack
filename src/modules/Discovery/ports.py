import socket
import coloredlogs, logging
import sys
import threading
from threading import Thread
import numpy

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
coloredlogs.install(logger=logger, level='DEBUG')


class PortScanner(object):
    def __init__(self, application):
        self.app = application
        self.ip = self.app.ip  # socket.gethostbyname(remoteServer)
        self.thread_number = 20

    def scan(self, from_port=1, to_port=1025, extra_ports=[]):
        lock = threading.Lock()
        openList = []
        all_ports = list(range(from_port, to_port)) + extra_ports
        chunks = numpy.array_split(numpy.array(all_ports), self.thread_number)
        threads = []
        for chunk in chunks:
            thread = Thread(target=_scan_ports, args=(lock, openList, self.ip, list(chunk)))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        return openList

def _scan_ports(lock, open_list, ip, ports):
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            result = sock.connect_ex((ip, port))
            if result == 0:
                lock.acquire()
                open_list.append(port)
                lock.release()
                logger.info("Port {:d} open".format(port))
                sock.close()
            else:
                logger.debug("Port {:d} closed".format(port))
        except KeyboardInterrupt:
            sys.exit()
        except:
            logger.debug("Port {:d} closed".format(port))
