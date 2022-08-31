from fastapi import Depends, FastAPI

app = FastAPI()

"""
An optional query parameter q that is a str.
An optional query parameter skip that is an int, and by default is 0.
An optional query parameter limit that is an int, and by default is 100
"""
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    # returns a dict
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
# Declare the dependency, in the "dependant". fungsi read_items memerlukan/memanggil/menjlnkan fungsi common_parameters
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
# Declare the dependency, in the "dependant". fungsi read_users memerlukan/memanggil/menjlnkan fungsi common_parameters
async def read_users(commons: dict = Depends(common_parameters)):
    return commons

# Classes as dependencies
# biasanya saat membuat instansiasi dr suatu class
class Cat:
    # constructor
    def __init__(self, name: str):
        self.name = name


fluffy = Cat(name="Mr Fluffy")
print(fluffy)

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/classASdependencies/items/")
# read_items akan menjlnkan/memanggil commons yg bertipe CommonQueryParams, sedangkan CommonQueryParams sendiri mrpkn suatu class CommonQueryParams
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response

# kode diatas (class as dependencies) akan sama dg kode dibawah (outputnya), kode dibawah dependency-nya berupa function
async def common_parameters_func(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/dependencyfunc/items/")
async def read_items(commons: dict = Depends(common_parameters_func)):
    return commons


@app.get("/dependencyfunc/users/")
async def read_users(commons: dict = Depends(common_parameters_func)):
    return commons

# cara diatas CommonQueryParams ditulis 2x, cara lainnya sbb
@app.get("/short1/items/")
async def read_items(commons=Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response

@app.get("/short2/items/")
async def read_items(commons: CommonQueryParams = Depends()):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response