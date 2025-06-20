# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/items/")
# async def create_item(item: Item):
#     total = item.price * item.quantity
#     return {
#         "name": item.name,
#         "price": item.price,
#         "quantity": item.quantity,
#         "total": total
#     }

# @app.get("/")
# async def root():
#     return {item}



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = []

@app.get("/")
def root():
    return {"Hello world"}


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items  

@app.get("items")
def list_items(limit: int = 10):
    return items[0:limit]


@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="item not found")