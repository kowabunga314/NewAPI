from sqlalchemy.orm import Session

from product.models import Product
from product.schema import ProductCreate


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def query_product(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):
    # db_product = Product(
    #     name=product.name,
    #     description=product.description,
    #     profit_margin=product.profit_margin,
    #     sku=product.sku,
    # )
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session):
    return None

def delete_product(db: Session):
    return None
