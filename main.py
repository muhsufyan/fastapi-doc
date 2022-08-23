from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
# default for skip is 0 and limit is 10
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

"""
optional query parameters
q will be optional, and will be None by default
"""
from typing import Union

@app.get("/items/{item_id}")
# for python 3.6
async def read_item(item_id: str, q: Union[str, None] = None):
# for python 3.10
# async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# for bool types will be convert. short can be foo?short=1 foo?short=yes foo?short=True foo?short=true foo?short=on
@app.get("/items/{item_id}")
# 3.6
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
# 3.10
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# multiple path parameters and query parameters at the same time
# user_id is path param, item_id is query param
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
# 3.10
# async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# make a query parameter required, not declare any default value
@app.get("/nodefault/required/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item
# define some parameters as required, some as having a default value, and some entirely optional:
@app.get("/campuran/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
# 3.10
# async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item