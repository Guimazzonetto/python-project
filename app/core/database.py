import config

from pymongo import MongoClient

client = MongoClient(config.MONGO_URI)
database = client[config.MONGO_DATABASE]

users_collection = database["users"]
category_collection = database["categories"]
transaction_collection = database["transactions"]