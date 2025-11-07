from fastapi import FastAPI

from app.routes import user


def Create_app():
  app = FastAPI()

  app.include_router(user.router)
  
  return app