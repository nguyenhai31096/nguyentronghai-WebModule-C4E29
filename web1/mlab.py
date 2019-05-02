from pymongo import MongoClient

uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(uri)
db = client.c4e
coll_river = db["river"]

rivers = coll_river.find({'continent':'Africa'})
list_rivers = []

for i in rivers:
    list_rivers.append(i['name'])

print(list_rivers)

rivers_america = coll_river.find({'continent':'S. America'})
list_river_america = []

for length_river in rivers_america:
    if length_river['length'] < 1000:
        list_river_america.append(length_river['name'])

print(list_river_america)