# provides all the functionality for our API.
from fastapi import FastAPI

app = FastAPI()

# http method lainnya .post() .put() .delete() .get() .options() .head() .patch() .trace()
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
# catch path param with argument func (item_id param read_item func will catch item_id data url) but the data from url is not define data type
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/search/item/{item_id}")
# catch path param with argument func (item_id param read_item func will catch item_id data url).
# and the data from url is must int
async def read_item(item_id: int):
    return {"item_id": item_id}

# pilih salah satu data dari list data (like gender, tingkatan/level). contoh model ml yg bisa dipilih
from enum import Enum
# list of model ML
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

"""
path param untuk file
ex path file home/johndoe/myfile.txt & url is /files/{file_path}
so url will be /files/home/johndoe/myfile.txt
"""
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}