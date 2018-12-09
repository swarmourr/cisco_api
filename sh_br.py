import json
from pyntc import ntc_device as NTC
from mongo_db_connect import *
import re
import schema

config = ConfigParser.ConfigParser()
config.read('adresse.conf')

iosvl2=NTC(host="192.168.122.215",username="hamza",password="hamza",device_type="cisco_ios_ssh")
iosvl2.open()
cmds = ['show ip route connected']
ios_output=iosvl2.show_list(cmds)
iosvl2.close()
list = '\n'.join(ios_output[0:])
list1=' '.join(list.split())
list1=list.split("\n")
backup=[]
for i in range(len(list1)):
      tmp = ' '.join(list1[i].split())
      list=tmp.split(" ")
      backup.append(list)

print "next router "
for i in range(len(config.items("hostnames"))) :
    dict={}
    network=[]
    interface=[]
    backuplist=[]
    hostname=config.items("hostnames")[i][0]
    print "router : "+hostname
    iosvl2=NTC(host=config.items("hostnames")[i][1],username="hamza",password="hamza",device_type="cisco_ios_ssh")
    iosvl2.open()
    cmds = ['show ip route connected']
    ios_output=iosvl2.show_list(cmds)
    iosvl2.close()
    list = '\n'.join(ios_output[0:])
    list1=' '.join(list.split())
    list1=list.split("\n")
    for i in range(len(list1)):
      tmp = ' '.join(list1[i].split())
      list=tmp.split(" ")
      for j in range(len(backup)):
          if list[1] == backup[j][1] :
              network.append(list[1])
              interface.append(list[5])
              backuplist.append(backup[j][5])
    dict={'hostname':hostname,'network':network,'interface':interface,'backup':backuplist}
    for i in range(len(dict['network'])) :
        print  "hostname :  " +   dict['hostname'] + " network  : " + dict['network'][i] +" interface : " + dict['interface'][i] + " backup : "+dict['backup'][i]
