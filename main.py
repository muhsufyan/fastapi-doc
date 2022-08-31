from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

# Response Status Code with status_code
@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item

# tags with a list of str
@app.post("/tags/items/", response_model=Item, tags=["items"])
async def create_item(item: Item):
    return item

@app.get("/tags/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]

@app.get("/tags/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]

# Tags with Enums
from enum import Enum
class Tags(Enum):
    items = "items"
    users = "users"


@app.get("/tags/enum/items/", tags=[Tags.items])
async def get_items():
    return ["Portal gun", "Plumbus"]


@app.get("/tags/enum/users/", tags=[Tags.users])
async def read_users():
    return ["Rick", "Morty"]

# Summary and description
@app.post(
    "/summaryANDdescription/items/",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
)
async def create_item(item: Item):
    return item

# Description from docstring
@app.post("/docstring/items/", response_model=Item, summary="Create an item")
async def create_item(item: Item):
    # INI
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

# Response description
# You can specify the response description with the parameter response_description
@app.post(
    "/responsedescription/items/",
    response_model=Item,
    summary="Create an item",
    # INI
    response_description="The created item",
)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

# Deprecate a path operation
# If you need to mark a path operation as deprecated, but without removing it, pass the parameter deprecated
@app.get("/deprecated/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/deprecated/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


@app.get("/deprecated/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]