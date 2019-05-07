from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@c4e29-cluster-chgml.mongodb.net/test?retryWrites=true"
client = MongoClient(uri)

bike_db = client.bike_db

rent_bike = bike_db['rent_bike']
