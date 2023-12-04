from fastapi import FastAPI
from sqlalchemy.orm import Session

from api.api import router
from api.database import SessionLocal, engine


# models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(router, prefix='/api')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}
