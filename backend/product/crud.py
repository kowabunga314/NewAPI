from main import app
from NewAPI.backend.product.schema import Product, Supply
from typing import Any


# Products

@app.get("/product/{product_id}/", response_model=Product)
async def read_product(product_id) -> Any:
    return None

@app.get("/product/", response_model=list[Product])
async def query_product() -> Any:
    return None

@app.put("/product/", response_model=Product)
async def create_product() -> Any:
    return None

@app.post("/product/", response_model=Product)
async def update_product() -> Any:
    return None

@app.delete("/product/")
async def delete_product() -> Any:
    return None


# Supplies

@app.get("/supply/{supply_id}/", response_model=Supply)
async def read_supply(supply_id) -> Any:
    return None

@app.get("/supply/", response_model=list[Supply])
async def query_supply() -> Any:
    return None

@app.put("/supply/", response_model=Supply)
async def create_supply() -> Any:
    return None

@app.post("/supply/", response_model=Supply)
async def update_supply() -> Any:
    return None

@app.delete("/supply/")
async def delete_supply() -> Any:
    return None