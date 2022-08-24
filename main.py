from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# declare data model as a class that inherits from BaseModel. data model ini digunakan untuk catch data dari request body. ini juga berguna untuk validasi data
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    # 3.10
    # description: str | None = None
    price: float
    tax: Union[float, None] = None
    # 3.10
    # tax: float | None = None

app = FastAPI()

@app.post("/items/")
# declare data model as param so can catch the data from request body
async def create_item(item: Item):
    return item

# gunakan data model, ex menghitung tax
@app.post("/usedatamodel/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    # jika ada data tax
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# request body + path param
@app.put("/reqbody/pathparam/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

# request body + path param + query param
"""
If the parameter is also declared in the path, it will be used as a path parameter.
If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.
"""
@app.put("/reqbody/pathparam/queryparam/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    # 3.6
# async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result