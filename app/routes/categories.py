from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pymongo.errors import DuplicateKeyError

from ..database.schema import Categories
from ..service.database.get_categories import get_categories_by_name
from ..core.database import category_collection
from ..core.logging import logger

router = APIRouter(
  prefix="/category",
  tags=["Category"]
)

@router.post("/new_category")
async def create_category(category: Categories):
  try:
    category_collection.insert_one(category.model_dump(by_alias=True))
    logger.info(f'Category {category.name} created successfully')
    return JSONResponse(
      content={"message": "Category created successfully"},
      status_code=201
    )
  
  except DuplicateKeyError:
    logger.warning(f'Duplicate category name attempted: {category.name}')
    return JSONResponse(
      content={"error": "Category name already registered"},
      status_code=409
    )
  
  except Exception as e:
    logger.exception(f'Error while check user in databse {e}')
    return JSONResponse(
      content={"error": "Databse error"},
      status_code=500
    )

@router.get("/categories")
async def get_all_categories():
  try:
    categories = list(category_collection.find({}))

    if categories:
      for c in categories:
        c["_id"] = str(c["_id"])

      logger.info("Categories finded")
      return JSONResponse(
        content={
          "message": "Categories finded",
          "Categories": categories
        },
        status_code=200
      )
    else:
      logger.info('Não foram encontradas categorias cadastradas')
      return JSONResponse(
        content={"message": "Não foram encontradas categorias cadastradas"},
        status_code=404
      )
  except Exception as e:
    logger.exception(f'Error while searching categories: {e}')
    return JSONResponse(
      content={"message": "Internal server error"},
      status_code=500
    )