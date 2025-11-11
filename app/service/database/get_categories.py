from ...core.database import category_collection
from ...core.logging import logger

async def get_categories_by_name(category_name: str):
  try:
    result = category_collection.find_one({"name": category_name})
    if result:
      logger.info("Category finded")
      return result
    else:
      logger.info("Category not finded")
      return None
    
  except Exception as e:
    logger.exception(f"The following error occured while get category: {e}")