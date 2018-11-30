import ConfigParser
import sys
import json
from pyntc import ntc_device as NTC
from mongo_db_connect import *
import re

tab=[]
config = ConfigParser.ConfigParser()
config.read('adresse.conf')
"""config.add_section("hostnames")
for i in range(len(config.items("routers"))) :
        iosvl2=NTC(host=config.items("routers")[i][1], username="hamza", password="hamza",device_type="cisco_ios_ssh")
        iosvl2.open()
        ios_output=iosvl2.facts
        iosvl2.close()
        config.set("hostnames",config.items("routers")[i][1],ios_output["hostname"])

with open('adresse.conf', 'w') as configfile:
    config.write(configfile)"""

# print config.items("hostnames")[0][0]
for i in range(len(config.items("hostnames"))) :
        tab.append(config.items("hostnames")[i][0])

for i in tab : 
        print i
