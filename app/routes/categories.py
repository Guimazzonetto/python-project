from fastapi import APIRouter
from fastapi.responses import JSONResponse

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
    result = await get_categories_by_name(category.name)
    if not result:
      try:
        category_collection.insert_one(category.model_dump(by_alias=True))
        logger.info("Category created with success")
        return JSONResponse(
          content={"message": "Category created successfully"},
          status_code=201
        )
      
      except Exception as e:
        logger.exception(f'Error while save new category in database: {e}')
        return JSONResponse(
          content={"message": "Error while saving category"},
          status_code=500
        )
    else:
      logger.info(f'Category exists')
      return JSONResponse(
        content={"message": "Category already exist"},
        status_code=409
      )

  except Exception as e:
    logger.exception(f'Error while check category in database {e}')
    return JSONResponse(
      content={"error": "Database error"},
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