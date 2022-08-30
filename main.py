# untuk menggunakan response model gunakan param response_model
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

# data yg diberikan kepada user as response data model adlh data dlm class Item
@app.post("/inputoutputaresame/items/", response_model=Item)
async def create_item(item: Item):
    return item

"""
FastAPI will use this response_model to:

Convert the output data to its type declaration.
Validate the data.
Add a JSON Schema for the response, in the OpenAPI path operation.
Will be used by the automatic documentation systems.
"""

# Return the same input data
from pydantic import EmailStr
# declaring a UserIn model, it will contain a plaintext password
class UserIn(BaseModel):
    username: str
    # Don't do this in production! because password should not show to user and must encrypted
    password: str
    email: EmailStr
    full_name: str | None = None
# declare our input and the same model to declare our output. this is very bad, lbh baik data model input dan output (response) itu berbeda & dipisah
@app.post("/user/", response_model=UserIn)
async def create_user(user: UserIn):
    return user

# Add an output model
# kita pisahkan antara data model input & output (response)
# dimana password tdk akan ditampilkan (as response data model)
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/inputoutputdifferent/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user

# Response Model encoding parameters
# response model could have default values
class Item2(BaseModel):
    name: str
    # defaultnya None
    description: str | None = None
    price: float
    # defaultnya 10.5
    tax: float = 10.5
    # # defaultnya list kosong
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

# You can set the path operation decorator parameter response_model_exclude_unset=True
"""
default values won't be included in the response, only the values actually set.
So, if you send a request to that path operation for the item with ID foo, the response (not including default values) will be:
{
    "name": "Foo",
    "price": 50.2
}
selain itu bisa juga memakai 
response_model_exclude_defaults=True
response_model_exclude_none=True
"""
@app.get("/responsemodel/defaultvalue/items/{item_id}", response_model=Item2, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]

# response_model_include and response_model_exclude
# ke2 nya disbt as path operation decorator
"""
They take a set of str with the name of the attributes to include (omitting the rest) or to exclude (including the rest).
This can be used as a quick shortcut if you have only one Pydantic model and want to remove some data from the output.

NOTE
still recommended to use the ideas above, using multiple classes, instead of these parameters.
This is because the JSON Schema generated in your app's OpenAPI (and the docs) will still be the one for the complete model, even if you use response_model_include or response_model_exclude to omit some attributes.
This also applies to response_model_by_alias that works similarly.
"""
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    # BAGIAN INI
    # The syntax {"name", "description"} creates a set with those two values. It is equivalent to set(["name", "description"]).
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]

# BAGIAN INI
@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]