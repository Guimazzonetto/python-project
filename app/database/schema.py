from typing import Optional

from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
  name: str
  email: str
  password: str

class Categories(BaseModel):
  name: str
  type: str

class Transactions(BaseModel):
  value: float
  description: str
  date: datetime
  type: str
  category_id: int
  user_id: int
