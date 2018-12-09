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
    if  number > 90 :
        iosvl2=NTC(host=config.get("hostnames",name),username="hamza",password="hamza",device_type="cisco_ios_ssh")
        iosvl2.open()
        s=get_int_backup(name)
        for i in range(len(s)):
            int = s[i]["interface_name"]
            cmds = [' ip int ' + int , 'ip policy route-map backup']
            ios_output=iosvl2.config_list(cmds)
            iosvl2.close()
    elif number > 80 & number < 90 :
        iosvl2=NTC(host=config.get("hostnames",name),username="hamza",password="hamza",device_type="cisco_ios_ssh")
        iosvl2.open()
        cmds = ['access-list 100 permit any any','route-map back_up permit 10','match ip address 100','set ip interface','set default interface']
        ios_output=iosvl2.config_list(cmds)
        iosvl2.close()
    elif number > 70 & number < 80:
        back_up(name)
    else  :
        print "good"

if __name__ == '__main__':
    ram_timer()
