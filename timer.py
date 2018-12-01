import threading
from connection import *
import threading, time, sys

config = ConfigParser.ConfigParser()
config.read('adresse.conf')

def ram_timer():
     for i in range(len(config.items("hostnames"))) :
                print " addiing ram to " + config.items("hostnames")[i][0]
                name = ram(config.items("hostnames")[i][0])
                decision(ram_super(name),name)

                time.sleep(10)
     ram_timer()

def decision(number,name) :
    if number > 90 :
        print "urgent"
    elif number > 75 & number < 85:
        back_up(name)
    else  :
        print " good"


if __name__ == '__main__':
    ram_timer()
