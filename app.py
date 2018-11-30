#!flask/bin/python
from flask import Flask,jsonify,abort,request
from connection import *
from mongo_db_connect import *
import json
from timer import *
import threading
from threading import Thread
import thread
from flask import Flask, render_template
import pymongo
import ConfigParser
import schema
config = ConfigParser.ConfigParser()
config.read('adresse.conf')

app=Flask(__name__)

@app.route("/")
def chart():
    list = value("Charge")
    labels = list[1]
    values = list[0]
    max1= max(values)
    list1 = value("Free")
    labels1 = list1[1]
    values1 = list1[0]
    max2= max(values1)
    dist={"CHARGE":list,"FREE":list1}
    #return render_template('test.html', values=values, labels=labels, maximum=max1 , values1=values1, labels1=labels1, maximum1=max2)
    return jsonify(dist)
# link to add infortion to the database
@app.route("/<string:name>/type")
def information_add(name):
    return  jsonify(facts(name))

#link to get routers info from  the database
@app.route("/<string:name>/info")
def information_get(name):
    return  jsonify(info(name))

#link to backup the routers configuration
@app.route("/<string:name>/back")
def back(name):
    return  json.dumps(back_up(name) , indent=4)

#link to update the route table
@app.route("/<string:name>/tab_route")
def tab_route(name):
    return  tab_routes(name)

#link to get router table
@app.route("/<string:name>/route")
def rout(name):
    return   jsonify(routes(name))

# link to get interfaces informations
@app.route("/<string:name>/interface/<path:name_int>")
def interface_info(name,name_int):
    return   jsonify(interface(name,name_int))

#link to get hostname
@app.route("/<string:name>/hostname")
def host(name):
    return jsonify(hostname(name))

@app.route("/<string:name>/ram")
def ram_use(name):
    return   jsonify(ram_tab(name))

#information to add ram variation to  db
@app.route("/<string:name>/ram_add")
def ram_us(name):
    return   jsonify(ram(name))

if __name__ == '__main__' :
    #thread.start_new_thread(app.run(debug=True,host=config.get('server', 'ip'), port=config.get('server','port')))
    #thread.start_new_thread(ram_timer())

    # print configuration()
    #Thread(target =ram_timer() ).start()
    Thread(target =app.run(debug=True,host=config.get('server', 'ip'), port=config.get('server','port'))).start()
