from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

# data model using pydantic, inherit BaseModel, for catch data from request body
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str | None = None,
    # declare body parameters as optional, by setting the default to None
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

# Multiple body parameters
# add data model user. now we have multiple body param (item & user)
class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put("/multiplebodyparam/items/{item_id}")
# multiple body param (item as data model Item & user as data model User)
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

# Singular values in body
from fastapi import Body
# add 1 key baru yaitu importance yg diambil dari body 
@app.put("/singlularvalueinbody/items/{item_id}")
# data yg diambil dari body request adlh data model item, data model user & data dg key importance 
async def update_item(item_id: int, item: Item, user: User, importance: int = Body()):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

# Multiple body params and query
from typing import Union
#  by default, singular values are interpreted as query parameters, you don't have to explicitly add a Query
# 3.6 => q: Union[str, None] = None
# 3.10 => q: str | None = None
@app.put("/multiplebodyparamandquery/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    # tambah validasi
    importance: int = Body(gt=0),
    q: Union[str, None] = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results

# Embed a single body parameter
# Let's say you only have a single item body parameter from a Pydantic model Item. By default, FastAPI will then expect its body directly.
# But if you want it to expect a JSON with a key item and inside of it the model contents, as it does when you declare extra body parameters,
# you can use the special Body parameter embed => item: Item = Body(embed=True)
class Item2(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/embedsinglebodyparam/items/{item_id}")
# item: Item = Body(embed=True)
async def update_item(item_id: int, item: Item2 = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results