from enum import Enum
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Annotated


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
