import ConfigParser
import json
config = ConfigParser.ConfigParser()
config.read('adresse.conf')
for  i in  config.sections() :
     print i +" :  "
     print  json.dumps(dict(config.items(i)), indent=20)

print ((config.get('db_connection','port')).split(","))[0]
