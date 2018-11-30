import json
from pyntc import ntc_device as NTC
from mongo_db_connect import *
import re
iosvl2=NTC(host="192.168.122.252", username="hamza" , password="hamza" , device_type="cisco_ios_ssh")
iosvl2.open()
ios_output=iosvl2.facts
iosvl2.close()

print ios_output["hostname"]
