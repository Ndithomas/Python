from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List
from models import Product
from database import create_db, get_session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db()

@app.post("/api/product", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: Product, session: Session = Depends(get_session)):
    if product:
        raise HTTPException(status_code=409, detail="Products already exists")
    items[item.name] = item
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@app.get("/api/products/limit/{limit}", response_model=List[Product], status_code = status.HTTP_200_OK)
def get_products(limit: int, session: Session = Depends(get_session)):
    return session.exec(select(Product).limit(limit)).all()

@app.get("/api/product/{product_id}", response_model=Product, status_code = status.HTTP_200_OK)
def get_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/api/product/{product_id}", response_model=Product, status_code = status.HTTP_200_OK)
def update_product(product_id: int, new_data: Product, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product_data = new_data.dict(exclude_unset=True)
    for key, value in product_data.items():
        setattr(product, key, value)
    
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@app.delete("/api/product/{product_id}")
def delete_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    session.delete(product)
    session.commit()
    return {"ok": True}
