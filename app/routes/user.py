from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pymongo.errors import DuplicateKeyError

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
    users_collection.insert_one(user.model_dump(by_alias=True))
    logger.info(f'User {user.email} created successfully')
    return JSONResponse(
      content={"message": "User created successfully"},
      status_code=201
    )

  except DuplicateKeyError:
    logger.warning(f'Duplicate email attempted: {user.email}')
    return JSONResponse(
      content={"error": "Email already registered"},
      status_code=409
    )

  except Exception as e:
    logger.exception(f'Error while check user in database {e}')
    return JSONResponse(
      content={"error": "Database error"},
      status_code=500
    )
  
@router.get("/get_user/{email}")
async def get_user(email):
  try:
    result = await get_user_service(email)

    if result:
      result["_id"] = str(result["_id"])
      logger.info("User finded")
      return JSONResponse(
        content={"message": "User finded",
                "user": result},
        status_code=200
      )
    else:
      logger.info("User not found")
      return JSONResponse(
        content={"message": "User not found"},
        status_code=404
      )
  except Exception as e:
    logger.exception(f"Error while searching user: {e}")
    return JSONResponse(
      content={"message": "Internal server error"},
      status_code=500
    )
