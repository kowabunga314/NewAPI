from fastapi import FastAPI
from sqlalchemy.orm import Session

from core.api import router


# models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(router, prefix='/api')


@app.get("/")
async def root():
    return {"message": "Hello World"}
