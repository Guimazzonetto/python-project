from pydantic import BaseModel, Field

class User(BaseModel):
  name: str
  email: str
  password: str

class Categories(BaseModel):
  name: str
  type: str