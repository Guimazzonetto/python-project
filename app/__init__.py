from fastapi import FastAPI

from app.routes import user, categories


def Create_app():
  app = FastAPI()

  app.include_router(user.router)
  app.include_router(categories.router)
  
  return app