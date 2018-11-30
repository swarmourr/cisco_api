import mongoengine
from mongoengine import *
import datetime

class routing(Document):
        h=""
        type = mongoengine.StringField()
        interface_name  = mongoengine.StringField()
        network = mongoengine.StringField(unique=True)
        netmask = mongoengine.IntField()
#        Date =mongoengine.DateTimeField(primary_key=True,default=datetime.datetime.now)
        meta = {
         'collection': h# collection name
         }

class fact(Document):
        h=""
        ssh = mongoengine.DictField()
        fqdn = mongoengine.StringField()
        hostname = mongoengine.StringField(primary_key=True)
        interfaces = mongoengine.ListField(StringField(max_length=50))
        model = mongoengine.StringField()
        os=  mongoengine.StringField()
        serial_number=mongoengine.StringField()
        uptime= mongoengine.IntField()
        uptime_string=mongoengine.StringField()
        vendor=mongoengine.StringField()
        vlans=mongoengine.ListField(StringField(max_length=50))
        Date =mongoengine.DateTimeField(default=datetime.datetime.now)
        meta = {
         'collection': h# collection name
         }

class ram_mem(Document):
        #Hostname=mongoengine.StringField(primary_key=True)
        k=""
        Free  = mongoengine.FloatField()
        Total = mongoengine.FloatField()
        Used = mongoengine.FloatField()
        Date =mongoengine.DateTimeField(primary_key=True,default=datetime.datetime.now)
        Charge=mongoengine.FloatField()
        Free_ram=mongoengine.FloatField()
        meta = {
        'collection': k# collection name

        }


class Hostname(Document):
        Hostname=mongoengine.StringField()

class charge(Document):
        Used =mongoengine.FloatField()
        Date =mongoengine.DateTimeField(primary_key=True , default=datetime.datetime.now)
        meta = {
        'collection': 'Charge' , # collection name
        }

class free(Document):
        Free =mongoengine.FloatField()
        Date =mongoengine.DateTimeField(primary_key=True , default=datetime.datetime.now)
        meta = {
        'collection': 'Free' , # collection name
        }

def add_one_route(dict,name) :
        mongoengine.connection.disconnect()
        s=connect("routes")
        post = routing(type=dict["type"],interface_name =dict["interface"] , network=dict["network"], netmask=int(dict["mask"]))
        post._meta['collection'] =dict["host"]
        post.save()
        s.close()
        return 1

def add_many_route(dict) :
        route=0
        mongoengine.connection.disconnect()
        s=connect("routes")
        for j in range(len(dict)):
            try :
               post =routing(type=dict[j]["type"],interface_name=dict[j]["interface"],network=dict[j]["network"], netmask=int(dict[j]["mask"]))
               post._meta['collection'] =dict["host"]
               post.save()
               route =route +1
            except :
               continue
        s.close()
        return route

def add_ram(dict) :
        mongoengine.connection.disconnect()
        s=connect("RAM")
        for j in range(len(dict)):
            try :
                post =ram_mem(Type=dict[j]["Type"],Total=int(dict[j]["Total"]), Used=int(dict[j]["Used"]),Free=int(dict[j]["Free"]))
                post._meta['collection'] = dict[0]['host']
                post.save()
            except Exception as e:
                print str(e)
        s.close()
#remplacer add ram
def add_ram1(dict) :
        mongoengine.connection.disconnect()
        s=connect("RAM")
        try :
           Somme = float(dict[0]["Total"])+float(dict[1]["Total"])
           Free = float(dict[0]["Free"])+float(dict[1]["Free"])
           Used = float(dict[0]["Used"])+float(dict[1]["Used"])
           ct_FREE=(Free*100)/Somme
           ct_used=(Used*100)/Somme
           post =ram_mem(Total=Somme, Used=Used,Free=Free,Charge=ct_used,Free_ram=ct_FREE)
           post._meta['collection'] = dict[0]['host']
           post.save()
           return  "done"
        except Exception as e:
                print str(e)
        s.close()
def add_charge(used) :
    s=connect("Ram")
    post =charge(Used=used)
    post.save()
    s.close()
    return 1

def add_free(free_ram) :
    mongoengine.connection.disconnect()
    connect("Ram")
    post =free(Free=free_ram)
    post.save()
    s.close()
    return 1

def add_info(dict) :
    mongoengine.connection.disconnect()
    s=connect("devices_informations")
    post =fact(ssh = dict["cisco_ios_ssh"],
    fqdn =dict['fqdn'],
    hostname =dict["hostname"],
    interfaces =dict["interfaces"],
    model = dict["model"],
    os=  dict["os_version"],
    serial_number=dict["serial_number"],
    uptime= dict["uptime"],
    uptime_string=dict["uptime_string"],
    vendor=dict["vendor"],
    vlans=dict["vlans"])
    post._meta['collection']=dict["hostname"]
    post.save()
    s.close()
    mongoengine.connection.disconnect()
    return "done"

def stop() :
    mongoengine.connection.disconnect()
