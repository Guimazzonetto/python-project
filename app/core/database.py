import config

from pymongo import MongoClient

client = MongoClient(config.MONGO_URI)
database = client[config.MONGO_DATABASE]

<<<<<<< HEAD

users_collection = database["users"]
categories_collection = database["categories"]
=======
users_collection = database["users"]
category_collection = database["categories"]
>>>>>>> ad39dc2f0c807e1e4cfebf4f0e2355c521b608e0
