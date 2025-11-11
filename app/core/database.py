import config

from pymongo import MongoClient

client = MongoClient(config.MONGO_URI)
database = client[config.MONGO_DATABASE]


users_collection = database["users"]
categories_collection = database["categories"]