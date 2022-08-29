from fastapi import Cookie, FastAPI

app = FastAPI()

# Declare Cookie parameters
# the same structure as with Path and Query
@app.get("/items/")
# The first value is the default value, you can pass all the extra validation or annotation parameters
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}