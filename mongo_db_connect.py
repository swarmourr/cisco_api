from pymongo import MongoClient
import json
import jsonschema
from schema import *
from mongo_db_connect import *
import pymongo
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('adresse.conf')

def connect(database,collection) :
    client = MongoClient()
    client = MongoClient(config.get('db_connection','ip'),int(((config.get('db_connection','port')).split(","))[0]), username=config.get('db_connection','username'),password=config.get('db_connection','pwd'))
    db = client[database]
    collection = db[collection]
    return collection

def insert_many(list) :
    mng_collection = connect()
    mng_collection.insert_many(list)

def insert_one(list) :
    mng_collection = connect()
    mng_collection.insert_one(list)

def find(name) :
    table_routage=[]
    mng_collection = connect(((config.get('db_name','name')).split(","))[1],name)
    for x in mng_collection.find({},{ "_id": 0 }):
      print x
      table_routage.append(x)
    return  table_routage

def find_ram(name) :
    ram=[]
    mng_collection = connect(((config.get('db_name','name')).split(","))[0],name)
    for x in mng_collection.find():
      print x
      ram.append(x)
    return ram
#ram calculfor different
def ram_calcul():
     result=[]
     mng_collection = connect(((config.get('db_name','name')).split(","))[1],config.get('Routing_collections','name'))
     for x in mng_collection.find().sort('_id',pymongo.DESCENDING).limit(2) :
         result.append(x)
     Somme = float(result[0]["Total"])+float(result[1]["Total"])
     Free = float(result[0]["Free"])+float(result[1]["Free"])
     Used = float(result[0]["Used"])+float(result[1]["Used"])
     ct_FREE=(Free*100)/Somme
     ct_used=(Used*100)/Somme
     add_charge(ct_used)
     add_free(ct_FREE)
     return

def value(collection_used) :
    result=[]
    result1=[]
    valeur=[]
    valeur1=[]
    dates=[]
    list=[]
    date=[]
    collection = connect("RAM",collection_used)
    """if collection_used == "Charge":
        u="Used"
    elif collection_used == "Free" :
        u="Free"
    else :
        return False"""
    for x in collection.find({},{ "_id": 0 ,"Charge" : 1 }).sort('_id',pymongo.DESCENDING).limit(30):
        result.append(x)
    # print " la chaaaaarge  derniere "
    for x in  collection.find({},{ "_id": 0 ,"Charge" : 1 }).sort('_id',pymongo.DESCENDING).limit(1):
        print x["Charge"]
    for x in collection.find({},{ "_id": 0 ,"Free_ram" : 1 }).sort('_id',pymongo.DESCENDING).limit(30):
        result1.append(x)
    for x in collection.find({},{ "_id": 1 }).sort('_id',pymongo.DESCENDING).limit(30):
        date.append(x)
    for i in range(len(result)):
      for key,val in result[i].items():
           valeur.append(val)

    for i in range(len(result1)):
      for key,val in result1[i].items():
           valeur1.append(val)

    for i in range(len(date)):
      for key,val in date[i].items():
           dates.append(val)
    list.append(valeur)
    list.append(valeur1)
    list.append(dates)
    max1= max(valeur)
    print " c la liste  : "
    print list
    return list

def info(name) :
    information=[]
    mng_collection = connect(((config.get('db_name','name')).split(","))[2],name)
    for x in mng_collection.find():
      print x
      information.append(x)
    return  information
