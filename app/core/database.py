import config

from pymongo import MongoClient, errors
from app.core.logging import logger

client = MongoClient(config.MONGO_URI)
database = client[config.MONGO_DATABASE]

users_collection = database["users"]
category_collection = database["categories"]
transaction_collection = database["transactions"]


# Transformando os campos "email" e "name" em únicos, assim não precisamos criar um id para as collections de usuário e categorias
try:
  users_collection.create_index("email", unique=True)
  category_collection.create_index("name", unique=True)
  logger.info("Unique indexes successfully created")
except errors.OperationFailure as e:
  logger.exception(f"Error creating indexes: {e}")



# Função para buscar o valor do campo ID no último documento da collection
def get_id(collection):
  last_item_id = collection.find_one(sort=[("id", -1)])
  if last_item_id:
    return last_item_id["id"] + 1
  else:
    return 1