import json
from pyntc import ntc_device as NTC
from mongo_db_connect import *
from schema import *
import re
import os
import sys

config = ConfigParser.ConfigParser()
config.read('adresse.conf')

def facts(name) :
    iosvl2=NTC(host=config.get("hostnames",name), username="hamza" , password="hamza" , device_type="cisco_ios_ssh")
    iosvl2.open()
    ios_output=iosvl2.facts
    iosvl2.close()
    return  add_info(ios_output,name)

def back_up(name) :
    iosvl2=NTC(host=config.get("hostnames",name), username="hamza" , password="hamza" , device_type="cisco_ios_ssh")
    iosvl2.open()
    ios_output=iosvl2.backup_running_config('ip.cfg')
    iosvl2.close()
    return "is back_uped "

def tab_routes(name) :
    substring = "C"
    table_routage=[]
    iosvl2=NTC(host=config.get("hostnames",name), username="hamza" , password="hamza" , device_type="cisco_ios_ssh")
    iosvl2.open()
    cmds = ['show ip route']
    ios_output=iosvl2.show_list(cmds)
    iosvl2.close()
    # h=hostname(name)
    list = '\n'.join(ios_output[0:])
    list1 = list.split("\n")
    for d in list1[10:] :
        if substring in d :
            rt = re.sub(' +',' ',d)
            d=rt.split(" ")
            way = {
                'type': d[0],
                'network': d[1].split("/")[0],
                'mask': d[1].split("/")[1],
                'interface': d[5],
                'host': name,
            }
            table_routage.append(way)
        else :
            continue
    if len(table_routage)==1:
            add_one_route(table_routage[0],name)
            return " 1 route added"
    elif len(table_routage) > 1:
        try:
            num=add_many_route(table_routage,name)
            return  str(num) + " route added "
        except:
              return  " NO route added "
    else :
        return "Oop"
    #return "new routes added to the, database"

def routes(name) :
    return find(name)

def interface(name_router,name) :
    iosvl2=NTC(host=config.get("hostnames",name_router), username="hamza" , password="hamza" , device_type="cisco_ios_ssh")
    iosvl2.open()
    cmds = ['show run interface '+ name +' br']
    ios_output=iosvl2.show_list(cmds)
    if name[0].lower()=='f' :
        iosvl2.close()
        list = '\n'.join(ios_output[0:])
        list1=list.split("ip ")
        list= ''.join(list1[1])
        list1=list.split("\n ")
        list= ('\n'.join(list1)).replace(" ", ":")
        list1=list.split("\n")
        network = {"name":name ,"ip":(list1[0].split(":"))[1], "duplex":(list1[1].split(":"))[1], "speed":(list1[2].split(":"))[1]}
    elif name[0].lower()=='s' :
        list = '\n'.join(ios_output[0:])
        list1=list.split("ip ")
        list= ''.join(list1[1])
        list1=list.split("\n ")
        list= ('\n'.join(list1)).replace(" ", "\n")
        list1=list.split("\n")
        network = {"ip":list1[1], "Mask":list1[2], "clock rate":list1[5]}
    elif name[0].lower()=='l' :
        network = "not yet done"
    return network

def ram(name) :
    iosvl2=NTC(host=config.get("hostnames",name), username="hamza" , password="hamza" , device_type="cisco_ios_ssh")
    iosvl2.open()
    cmds = ['show proc mem | inc Used']
    ios_output=iosvl2.show_list(cmds)
    iosvl2.close()
    list = '\n'.join(ios_output[0:])
    list1=list.split("\n")
    l1=(list1[0].replace("  ", " ")).split(" ")
    l2=(list1[1].replace("  ", " ")).split(" ")
    h=hostname(name)
    dict =[{'host': h["Hostname"] , 'Type':l1[0], 'Total':l1[3] ,'Used': l1[6] ,'Free':l1[8] },{'host': h,'Type':l2[3], 'Total':l2[7] ,'Used': l2[10] ,'Free':l2[13] }
    ]
    add_ram1(dict)

def ram_tab(name) :
    return find_ram(name)

def trace() :
     return value()

def hostname(name) :
    iosvl2=NTC(host=config.get("hostnames",name), username="hamza" , password="hamza" , device_type="cisco_ios_ssh")
    iosvl2.open()
    ios_output=iosvl2.facts
    iosvl2.close()
    dict ={'Hostname': ios_output["hostname"]}
    return dict

def configuration(i) :
  while(i==0):
    tab=[]
    config.remove_section("hostnames")
    config.add_section("hostnames")
    print  "the api is configuring ."
    for i in range(len(config.items("routers"))) :
            iosvl2=NTC(host=config.items("routers")[i][1], username="hamza", password="hamza",device_type="cisco_ios_ssh")
            iosvl2.open()
            ios_output=iosvl2.facts
            iosvl2.close()
            config.set("hostnames",ios_output["hostname"],config.items("routers")[i][1])
            print   str(i) + " :  configuring the router " + ios_output["hostname"]

    with open('adresse.conf', 'w') as configfile:
        config.write(configfile)
    for i in range(len(config.items("hostnames"))) :
            tab.append(config.items("hostnames")[i][0])

    for i in tab :
            facts(i)
            tab_routes(i)
