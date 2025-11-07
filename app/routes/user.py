from fastapi import APIRouter, Depends, HTTPException
from  ..database.schema import User
from ..core.database import users_collection
from ..core.logging import logger

router = APIRouter(
  prefix="/users",
  tags=["users"]
)

@router.post("/new_user")
async def create_user(user: User):
  try:
    # Faz com que o Schema seja entregue como JSON
    users_collection.insert_one(user.model_dump(by_alias=True))
    logger.info("User saved")

  except Exception as e:
    logger.exception("The following error occured: ", e)

  return user

@router.get("/get_user/:email")
async def get_user(user: User):
  return user