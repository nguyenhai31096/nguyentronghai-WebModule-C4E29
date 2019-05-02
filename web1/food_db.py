from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@c4e29-cluster-chgml.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)
food_db = client.food_database
Foods = food_db["food_collection"]

