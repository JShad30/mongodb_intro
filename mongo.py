import pymongo
import os

MONGO_URI = os.getenv("MONGO_URI")
DBS_NAME = "mytestdb"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo DB is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGO_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

#new_docs = [{'first_name': 'colin', 'last_name': 'turkington', 'dob': '21/03/1982', 'gender': 'm', 'hair_colour': 'brown', 'occupation': 'racing driver', 'nationality': 'northern irish'}, {'first_name': 'gordon', 'last_name': 'shedden', 'dob': '15/02/1979', 'gender': 'm', 'hair_colour': 'blonde', 'occupation': 'racing driver', 'nationality': 'scottish'}, {'first_name': 'al', 'last_name': 'unser', 'dob': '29/05/1939', 'gender': 'm', 'hair_colour': 'brown', 'occupation': 'racing driver', 'nationality': 'american'}]

#coll.insert_many(new_docs);

#documents = coll.remove({'gender': 'f'})

coll.update_many({'nationality': 'scottish'}, {'$set': { 'hair_colour': 'red'}})

documents = coll.find({'nationality': 'scottish'});

for doc in documents:
    print(doc)