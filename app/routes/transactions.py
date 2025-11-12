from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime

from ..database.schema import Transactions
from ..core.database import transaction_collection, get_id
from ..core.logging import logger

router = APIRouter(
  prefix="/transactions",
  tags=["transaction"]
)

@router.post("/new_transaction")
async def create_transactions(transaction: Transactions):
  try:
    item_id = get_id(transaction_collection)

    transaction_collection.insert_one({
      "id": item_id,
      **transaction.model_dump()
    })

    logger.info("Transaction created with success.")
    return JSONResponse(
      content={"message": "Transaction created successfully"},
      status_code=201
    )
  
  except Exception as e:
    logger.exception(f'Error while insert new transaction {e}')
    return JSONResponse(
      content={"error": "Error while save in database"},
      status_code=500
    )


# @router.get("/get_transaction/{id}")


@router.get("/all_transactions")
async def get_all_transactions():
  try:
    transactions = list(transaction_collection.find({}))
    
    if transactions:
      for t in transactions:
        if isinstance(t.get("date"), datetime):
          t["date"] = t["date"].isoformat()
        t["_id"] = str(t["_id"])

      logger.info("Transactions finded")
      return JSONResponse(
        content={
          "message": "Transactions",
          "Transactions": transactions
        },
        status_code=200
      )

  except Exception as e:
    logger.exception(f'Error while searching transactions: {e}')
    return JSONResponse(
      content={"message": "Internal server error"},
      status_code=500
    )