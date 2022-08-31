from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

"""
data model input-nya berupa pydantic melalui class Item kita akan update
dari pydantic model jd json
"""
class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]

# edit id item (convert) dari pydantic model jd json
# Warning : saat update bar atribut tax itu 20 sedangkan defaultnya 10, bisa saja nilai yg diambil adlh defaultnya bkn 20
# sedangkan untuk data yg tdk punya atribut tax akan diset default
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded

# Partial updates with PATCH
# mungkin kita hanya ingin mengubah data tertentu saja (tdk semua data) maka gunakan http PATCH bukan PUT

# Using Pydantic's exclude_unset parameter
# partial updates, very useful to use the parameter exclude_unset in Pydantic's model's .dict().
# contoh item.dict(exclude_unset=True)
# That would generate a dict with only the data that was set when creating the item model, excluding(tdk termasuk) default values
# Then you can use this to generate a dict with only the data that was set (sent in the request), omitting(menghilangkan) default values
@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item

# Using Pydantic's update parameter
"""
 you can create a copy of the existing model using .copy(),
 and pass the update parameter with a dict containing the data to update.
Like stored_item_model.copy(update=update_data)
"""
@app.patch("/pydanticupdateparameter/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item

# Partial updates recap, BACA DI DOC/README.md
@app.patch("/Partialupdatesrecap/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item