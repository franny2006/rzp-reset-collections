import json
import sys
from pymongo import MongoClient

configFile = '/app/config/collections.json'
print("\nImportierte Config-Datei:", configFile)


with open (configFile) as json_file:
    data = json.load(json_file)

print(data)

for connection in data['connections']:
    for collection in connection['collections']:
        print(connection['connectionName'], connection['connectionString'], connection['database'], collection['collectionName'])
        connClient = MongoClient(connection['connectionString'], uuidRepresentation="standard")
        connDb = connClient[connection['database']]
        connColl = connDb[collection['collectionName']]
        d = connColl.delete_many({})


