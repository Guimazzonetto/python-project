from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..database.schema import Categories
from ..core.database import categories_collection
from ..core.logging import logger

