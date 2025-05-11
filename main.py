from fastapi import FastAPI
# Initialize FastAPI app
app = FastAPI()

# Simple in-memory database
items = {}

# Hello World endpoint
@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}

# GET - Get all items
@app.get("/items")
def get_items():
    return items

# GET - Get a specific item
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id in items:
        return items[item_id]
    return {"error": "Item not found"}

# POST - Create an item
@app.post("/items")
def create_item(item_id: int, name: str, price: float = 0):
    items[item_id] = {"name": name, "price": price}
    return items[item_id]
# PUT - Update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, name: str = None, price: float = None):
    if item_id not in items:
        return {"error": "Item not found"}

    if name:
        items[item_id]["name"] = name
    if price is not None:
        items[item_id]["price"] = price

    return items[item_id]

# DELETE - Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        return {"error": "Item not found"}

    deleted = items.pop(item_id)
    return {"message": "Item deleted", "item": deleted}