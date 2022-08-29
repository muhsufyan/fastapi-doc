from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# List fields
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    # define an attribute to be a subtype with list. This will make tags be a list.  define an attribute to be a subtype
    tags: list = []

@app.put("/listfields/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# List fields with type parameter
# declare lists with internal types, or "type parameters". 
from typing import List, Union

class Item2(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    # use list to declare these type annotations
    tags: List[str] = []


@app.put("/withp=typeparam/items/{item_id}")
async def update_item(item_id: int, item: Item2):
    results = {"item_id": item_id, "item": item}
    return results

# Declare a list with a type parameter
# ex listnya (atau dict, tuple) berupa string/int
# => my_list: list[str] untuk v 3.9 keatas
# => from typing import List; my_list: List[str] untuk v 3.6
class Item3(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.put("/declaretypelistparam/items/{item_id}")
async def update_item(item_id: int, item: Item3):
    results = {"item_id": item_id, "item": item}
    return results

# Set types
# for make list (tags) is unique use "set"
class Item4(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    # declare tags as a set of strings
    tags: set[str] = set()

"""
now if you receive a request with duplicate data, it will be converted to a set of unique items.

And whenever you output that data, even if the source had duplicates, it will be output as a set of unique items.

And it will be annotated / documented accordingly too.
"""
@app.put("/settypes/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# Nested Models 
# maksud model disini adlh data model.
# setiap atribut dari pydantic memiliki tipe data bahkan tipe data dari data model lainnya
# define sub model (data model image as sub data model to Item5 data model)
class Image(BaseModel):
    url: str
    name: str


class Item5(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    # atribut image is sub model type are data model Image & Use the submodel as a type
    image: Image | None = None


@app.put("/submodel/items/{item_id}")
async def update_item(item_id: int, item: Item5):
    results = {"item_id": item_id, "item": item}
    return results
"""
dg demikian kita telah melakukan
Editor support (completion, etc), even for nested models
Data conversion
Data validation
Automatic documentation
"""

# Special types and validation
