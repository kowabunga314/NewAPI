from fastapi import FastAPI
from sqlalchemy.orm import Session
import uvicorn

from core.api import router


# models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(router, prefix='/api')


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
