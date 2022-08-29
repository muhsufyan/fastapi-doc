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
async def update_item(item_id: int, item: Item4):
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

# # Special types and validation
# # untuk melihat validasi tipe data lainnya https://pydantic-docs.helpmanual.io/usage/types/

from pydantic import HttpUrl 
class Image2(BaseModel):
    # contoh data model Image memiliki field bertipe url (string will be checked to be a valid URL)
    url: HttpUrl
    name: str


class Itemss(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image2 | None = None


@app.put("/tipespesialdanvalidasi/items/{item_id}")
async def update_item(item_id: int, item: Itemss):
    results = {"item_id": item_id, "item": item}
    return results

# Attributes with lists of submodels
class Item7(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    #  use Pydantic models as subtypes of list, set, etc
    images: list[Image2] | None = None


@app.put("/atributdglistsofsubmodels/items/{item_id}")
async def update_item(item_id: int, item: Item7):
    results = {"item_id": item_id, "item": item}
    return results

# Deeply nested models
class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item7]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

# Bodies of pure lists
"""
If the top level value of the JSON body you expect is a JSON array (a Python list),
you can declare the type in the parameter of the function, the same as in Pydantic models:
images: List[Image]
or in Python 3.9 and above:
images: list[Image]
"""
@app.post("/images/multiple/")
# ini dia
async def create_multiple_images(images: list[Image2]):
    return images

# Bodies of arbitrary dict
"""
You can also declare a body as a dict with keys of some type and values of other type
This would be useful if you want to receive keys that you don't already know.
"""
@app.post("/index-weights/")
# weight adlh dictionary dg jenis int dan float (2 tipe yg berbeda). 
# you would accept any dict as long as it has int keys with float values
async def create_index_weights(weights: dict[int, float]):
    return weights