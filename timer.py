import threading
from connection import *
import threading, time, sys

config = ConfigParser.ConfigParser()
config.read('adresse.conf')

def ram_timer():

     #threading.Timer(60.0, ram).start()
     #ram()
     #ram_calcul()
     for i in range(len(config.items("hostnames"))) :
                print " addiing ram to " + config.items("hostnames")[i][0]
                ram(config.items("hostnames")[i][0])
                time.sleep(10)
     ram_timer()


if __name__ == '__main__':
    ram_timer()
