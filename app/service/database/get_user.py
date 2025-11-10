from ...database.schema import User
from ...core.database import users_collection
from ...core.logging import logger

async def get_user(user_email: str):
  try:
    result = users_collection.find_one({"email": user_email})
    if result:
      logger.info(f'User finded')
      return result
    else:
      logger.info(f'User not finded')
      return None

  except Exception as e:
    logger.exception(f"The following error occured: {e}")
