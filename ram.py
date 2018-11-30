import json
from pyntc import ntc_device as NTC
from mongo_db_connect import *
import re

iosvl2=NTC(host="192.168.122.252", username="hamza" , password="hamza" , device_type="cisco_ios_ssh")
iosvl2.open()
cmds = ['show proc mem | inc Used']
list_find=["^Total: ","^Used:  ","^Free: "]
ios_output=iosvl2.show_list(cmds)
list = '\n'.join(ios_output[0:])
list1=list.split("\n")
l1=(list1[0].replace("  ", " ")).split(" ")
l2=(list1[1].replace("  ", " ")).split(" ")
dict =[{'Type':l1[0], 'Total':l1[3] ,'Used': l1[6] ,'Free':l1[8] },{'Type':l2[3], 'Total':l2[7] ,'Used': l2[10] ,'Free':l2[13] }
]
print  dict[0]["Type"]

print json.dumps(dict)
