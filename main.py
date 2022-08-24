from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
# param q bertipe string & jika tdk diisi defaultnya None. disini blm kita tambah validasi untuk paramnya (berupa q)
async def read_items(q: Union[str, None] = None):
# 3.10
# async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
"""
MENAMBAHKAN VALIDASI UNTUK INPUT USER KASUS QUERY PARAM
pertama kita perlu import query
"""
from fastapi import FastAPI, Query

@app.get("/validationqueryparam/qismax50/items/")
# validasinya berupa max karakter 50, dg set default=None artinya param tsb not required.
# nilai default dpt berupa yg lainnya sprti default="fixedquery"
async def read_items(q: str | None = Query(default=None, max_length=50)):
    # 3.6
# async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# more validations
@app.get("/validationqueryparam/qismin3&max50/items/")
async def read_items(
    q: Union[str, None] = Query(default=None, min_length=3, max_length=50)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# validasi regex
"""
^: starts with the following characters, doesn't have characters before.
fixedquery: has the exact value fixedquery.
$: ends there, doesn't have any more characters after fixedquery
"""
@app.get("/validationqueryparam/regex/items/")
async def read_items(
    q: Union[str, None] = Query(
        default=None, min_length=3, max_length=50, regex="^fixedquery$"
    )
):
# 3.10
# async def read_items(q: str | None = Query(default=None, min_length=3, max_length=50, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# declare a value as required while using Query. 
# cara 1 dg not declare default value
@app.get("/Querywithrequired/cara1/items/")
# cara paling sederhana dg not declare a default value
async def read_items(q: str = Query(min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# cara 2 dg Required with Ellipsis (...)
# alternative way to explicitly declare that a value is required. You can set the default parameter to the literal value ...
@app.get("/Querywithrequired/cara2/items/")
# This will let FastAPI know that this parameter is required. dg tanda ... (literal value)
async def read_items(q: str = Query(default=..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Required with None
#  declare that a parameter can accept None, but that it's still required. This would force clients to send a value, even if the value is None
@app.get("/requiredwithNone/items/")
async def read_items(q: str | None = Query(default=..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Pydantic's Required
from pydantic import Required
@app.get("/requiredwithpydantic/items/")
async def read_items(q: str = Query(default=Required, min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Query parameter list / multiple values
# http://localhost:8000/items/?q=foo&q=bar
# When you define a query parameter explicitly with Query you can also declare it to receive a list of values, or said in other way, to receive multiple values
@app.get("/items/")
# declare a query parameter q that can appear multiple times in the URL
async def read_items(q: list[str] | None = Query(default=None)):
    # version 3.9 for 3.6 just change list to List
# async def read_items(q: Union[list[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items

# Query parameter list / multiple values with defaults
from typing import List
# define a default list of values if none are provided
@app.get("/queryparamlistdefaults/items/")
async def read_items(q: List[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items

# Using list
@app.get("/queryparamlistdefaults/usinglist/items/")
async def read_items(q: list = Query(default=[])):
    query_items = {"q": q}
    return query_items

# Declare more metadata
# menambahkan informasi dlm OpenAPI
@app.get("/metadata/title/items/")
async def read_items(
    q: Union[str, None] = Query(default=None, title="Query string", min_length=3)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# add deskripsi
@app.get("/metadata/title/description/items/")
async def read_items(
    q: str
    | None = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Alias parameters
"""
ex we want param are item-query the url .../?item-query=foobaritems. the param not valid in python but we need it 
so the solution is use alias to find the parameter value
"""
@app.get("/aliasparam/items/")
async def read_items(q: str | None = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Deprecating parameters
# make openapi clear from depricate add deprecated=True as param
@app.get("/depricated/items/")
async def read_items(
    q: str
    | None = Query(
        default=None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Exclude from OpenAPI
"""
To exclude(mengecualikan) a query parameter from the generated OpenAPI schema(from automatic documentation systems)
set the parameter include_in_schema of Query to False
"""
@app.get("/excludefromopenAPI/items/")
async def read_items(
    hidden_query: str | None = Query(default=None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}