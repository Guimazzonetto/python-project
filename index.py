import uvicorn
import logging


from app import Create_app
from app.core.logging import logger
from app.core.database import database

app = Create_app()

if __name__ == '__main__':

  try:
    database.list_collection_names()
    logger.info("Connected Successfully")
    
    uvicorn.run(app)

  except Exception as e:
    logger.exception("The following error occured: ", e)
