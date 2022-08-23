# provides all the functionality for our API.
from fastapi import FastAPI

app = FastAPI()

# http method lainnya .post() .put() .delete() .get() .options() .head() .patch() .trace()
@app.get("/")
async def root():
    return {"message": "Hello World"}