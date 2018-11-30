import json
from pyntc import ntc_device as NTC
import re
from mongo_db_connect import *


table_routage=[]
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.route
collection = db.route
for x in collection.find({},{ "_id": 0 }):
  print x
  table_routage.append(x)

print json.dumps(table_routage)
