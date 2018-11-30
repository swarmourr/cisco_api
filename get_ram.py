from pymongo import MongoClient
import pymongo
import json
import jsonschema


client = MongoClient()
client = MongoClient('localhost', 27017)
result=[]
date=[]
db = client.RAM
collection = db.Charge
collection1 = db.Free
for x in collection.find({},{ "_id": 0 }).sort('_id',pymongo.DESCENDING):
    result.append(x)
for x in collection.find({},{ "Used": 0 }).sort('_id',pymongo.DESCENDING):
    date.append(x)
"""
Somme = float(result[0]["Total"])+float(result[1]["Total"])
Free = float(result[0]["Free"])+float(result[1]["Free"])
Used = float(result[0]["Used"])+float(result[1]["Used"])
ct_FREE=(Free*100)/Somme
ct_used=(Used*100)/Somme

print result
print "Somme est : " + str(Somme)
print "Free est : " + str(Free)
print "Used est : " + str(Used)
print  str(ct_FREE) + "%"
print  str(ct_used) + "%"
print  " le taux erreur est : " + str(100 - (ct_FREE+ct_used)) +" % """

#print date
valeur=[]
dates=[]
list=[]
for i in range(len(result)):
  for key,val in result[i].items():
       valeur.append(val)

for i in range(len(date)):
  for key,val in date[i].items():
       dates.append(val)
list.append(valeur)
list.append(dates)

print list
