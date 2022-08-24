from fastapi import FastAPI, Path, Query

app = FastAPI()

# Declare metadata
# can declare all the same parameters as for Query
@app.get("/items/{item_id}")
async def read_items(
    # declare a title metadata value for the path parameter item_id
    item_id: int = Path(title="The ID of the item to get"),
    q: str | None = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
# SKIP DULU
# SKIP DULU
# SKIP DULU

# Number validations: greater than and less than or equal
"""
gt: greater than
le: less than or equal
"""
@app.get("/validasiangka/items/{item_id}")
async def read_items(
    *,
    # 0 <= item_id >= 1000
    item_id: int = Path(title="The ID of the item to get", gt=0, le=1000),
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# Number validations: floats, greater than and less than
"""
value must be greater than 0, even if it is less than 1.
So, 0.5 would be a valid value. But 0.0 or 0 would not.
"""
@app.get("/validasiangka/float/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

"""
With Query, Path (and others you haven't seen yet) you can declare metadata and string validations in the same ways as with 5-validasiqueryparam
And you can also declare numeric validations:
* gt: greater than
* ge: greater than or equal
* lt: less than
* le: less than or equal
"""