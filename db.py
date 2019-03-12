
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["User"]
#db.collection.Collection.delete_many({})
indexes: pymongo.collection.Collection = db["indexes"]
