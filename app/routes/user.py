from fastapi import APIRouter, Depends, HTTPException
from  ..database.schema import User
from ..core.database import users_collection
from ..core.logging import logger
from ..service.database.get_user import get_user as get_user_service

router = APIRouter(
  prefix="/users",
  tags=["users"]
)

@router.post("/new_user")
async def create_user(user: User):
  try:
    result = await get_user_service(user.email)
    if not result:
      try:
        # Faz com que o Schema seja entregue como JSON
        users_collection.insert_one(user.model_dump(by_alias=True))
        logger.info("User saved with success")
      
      except Exception as e:
        logger.exception(f'Error while save new user in database: {e}')
    
    else:
      logger.info(f'User exists')

  except Exception as e:
    logger.exception(f'Error while get user in database {e}')

  return user

@router.get("/get_user/{email}")
async def get_user(email):
  result = await get_user_service(email)
  if result:
    logger.info("User finded")
  else:
    logger.info("User not finded")
  result["_id"] = str(result["_id"])
  return result