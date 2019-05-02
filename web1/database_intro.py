from pymongo import MongoClient
from bson.objectid import ObjectId
uri = "mongodb+srv://admin:admin@c4e29-cluster-chgml.mongodb.net/test?retryWrites=true"

#1. create connection
client = MongoClient(uri)

#2. Get/ create database
first_db = client.first_database

#3. Get/ create collection
first_coll = first_db["first_collection"]

#4. Create document
# first_document = {
#     "game" : "Dota",
#     "description": "MOBA",
# }

game_list = {
    "game" : "Dota",
    "description": "MOBA",
},
{
    "game" : "FO4",
    "description": "Football game"
}
#5. Create
#5.1 Create one
# first_coll.insert_one(first_document)
#5.2 Create many
# first_coll.insert_many(game_list)

#6. READ
#6.1 read all
all_games = first_coll.find()
# lazy loading

# for game in all_games:
#     print(game)
#6.2 read one
# dota_game = first_coll.find_one({'_id': ObjectId('5cc064ccf7ea07efbe5427b1')})
# print(dota_game)

#7. Update
dota_game = first_coll.find_one({'_id': ObjectId('5cc05e3d2ce148cf5c7476cb')})
new_value = { "$set": { "game": "Auto chess" } }
first_coll.update_one(dota_game, new_value)
#8. Delete
dota_game = first_coll.find_one({'_id': ObjectId('5cc05e3d2ce148cf5c7476cb')})
if dota_game is not None:
    first_coll.delete_one(dota_game)
else:
    print("NOT FOUND!")
