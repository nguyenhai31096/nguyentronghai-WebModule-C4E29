from pymongo import MongoClient
from bson.objectid import ObjectId
from matplotlib import pyplot
uri ="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.c4e
# coll = db["posts"]
# stt_list = {
#     "title" : "Loving you",
#     "author": "Hải Nguyễn",
#     "content": "Nói lời chân thật với nhau, đừng bắt tâm tư phải sàng và lọc",
# }
# coll.insert_one(stt_list)

#ex_3:

coll_custom = db["customers"]
events = coll_custom.find({'ref': 'events'})
events_count = events.count()
wom = coll_custom.find({'ref': 'wom'})
wom_count = wom.count()
ads = coll_custom.find({'ref': 'ads'})
ads_count = ads.count()
#count
print(wom_count)
print(events_count)
print(ads_count)
#chart
labels = 'Events', 'Word of mouth', 'Ads'
sizes = [events_count,wom_count,ads_count]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

pyplot.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

pyplot.axis('equal')
pyplot.show()





