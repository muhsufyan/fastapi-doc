# Add dependencies to the path operation decorator

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()

# Dependency requirements. declare request requirements (like headers) or other sub-dependencies
async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        # dependencies can raise exceptions, the same as normal dependencies
        raise HTTPException(status_code=400, detail="X-Token header invalid")
        # can return values or not, the values won't be used. FOR THIS NOT RETURN VALUE

# Dependency requirements. declare request requirements (like headers) or other sub-dependencies
async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        # dependencies can raise exceptions, the same as normal dependencies
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    # can return values or not, the values won't be used. FOR THIS RETURN VALUE
    return x_key

# path operation decorator receives an optional argument dependencies. It should be a list of Depends()
# return value (if they return any) won't be passed to your path operation function but the dependencies will be executed
@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]

# GLOBAL DEPENDENCY
# if want add dependencies to the whole application

# THIS GLOBAL DEPENDENCY
app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/withglobaldependencies/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@app.get("/withglobaldependencies/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]