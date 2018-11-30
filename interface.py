import json
from pyntc import ntc_device as NTC
from mongo_db_connect import *
import re

iosvl2=NTC(host="192.168.122.252",username="hamza",password="hamza",device_type="cisco_ios_ssh")
iosvl2.open()

cmds = ['show run | inc host']

ios_output=iosvl2.show_list(cmds)
print ios_output

"""list = '\n'.join(ios_output[0:])
list1=list.split("ip ")
list= ''.join(list1[1])
list1=list.split("\n ")
list= ('\n'.join(list1)).replace(" ", "\n")
list1=list.split("\n")
network = {"ip":list1[1], "Mask":list1[2], "clock rate":list1[5]}
print network"""
