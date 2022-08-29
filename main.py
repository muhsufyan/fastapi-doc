from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
#  can declare an example for a Pydantic model using Config and schema_extra
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# Field additional arguments
# When using Field() with Pydantic models, you can also declare extra info for the JSON Schema by passing any other arbitrary arguments to the function
from pydantic import Field
class Item2(BaseModel):
    # add example for each field. cara lain selain menggunakan Config and schema_extra
    name: str = Field(example="Foo")
    description: str | None = Field(default=None, example="A very nice Item")
    price: float = Field(example=35.4)
    tax: float | None = Field(default=None, example=3.2)


@app.put("/fieldaddarg/items/{item_id}")
async def update_item(item_id: int, item: Item2):
    results = {"item_id": item_id, "item": item}
    return results

# example and examples in OpenAPI
"""
When using any of:
Path(), Query(), Header(), Cookie(), Body(), Form(), File()
you can also declare a data example or a group of examples with additional information that will be added to OpenAPI.
"""
# Body with example

from fastapi import Body
class Item3(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/bodydgex/items/{item_id}")
async def update_item(
    item_id: int,
    # pass an example of the data expected in Body()
    item: Item3 = Body(
        example={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results

# Body with multiple examples
# pass examples using a dict with multiple examples, each with extra information that will be added to OpenAPI too
"""
Each specific example dict in the examples can contain:

summary: Short description for the example.
description: A long description that can contain Markdown text.
value: This is the actual example shown, e.g. a dict.
externalValue: alternative to value, a URL pointing to the example. Although this might not be supported by as many tools as value.
"""
@app.put("/bodydgmultipleex/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item3 = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results

# tipe data lainnya
# terdpt tipe data lainnya selain int, str, dll. 
# liat bagian ini https://fastapi.tiangolo.com/tutorial/extra-data-types/ untuk penjelasan
from datetime import datetime, time, timedelta
from uuid import UUID
@app.put("/othertype/items/{item_id}")
async def read_items(
    # contoh tipe data yg lainnya
    item_id: UUID,
    start_datetime: datetime | None = Body(default=None),
    end_datetime: datetime | None = Body(default=None),
    repeat_at: time | None = Body(default=None),
    process_after: timedelta | None = Body(default=None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }

# kita juga bisa melakukan manipulasi/suatu proses
@app.put("/manipulation/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: datetime | None = Body(default=None),
    end_datetime: datetime | None = Body(default=None),
    repeat_at: time | None = Body(default=None),
    process_after: timedelta | None = Body(default=None),
):
# proses / manipulasi (kalkulasi)
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }