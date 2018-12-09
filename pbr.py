""""""
import json
from pyntc import ntc_device as NTC
from mongo_db_connect import *
import re
import schema
import mongo_db_connect



s=get_int_backup("r1")
for i in range(len(s)):
    print s[i]["interface_name"]
"""
config = ConfigParser.ConfigParser()
config.read('adresse.conf')

iosvl2=NTC(host="192.168.122.215",username="hamza",password="hamza",device_type="cisco_ios_ssh")
iosvl2.open()
cmds = ['access-list 100 permit any any','route-map back_up permit 10','match ip address 100','set ip interface','set default interface',' ip int ' , 'ip policy route-map backup']
ios_output=iosvl2.(cmds)
iosvl2.close()
list = '\n'.join(ios_output[0:])
list1=' '.join(list.split())
list1=list.split("\n")
backup=[]
for i in range(len(list1)):
      tmp = ' '.join(list1[i].split())
      list=tmp.split(" ")
      backup.append(list)"""
