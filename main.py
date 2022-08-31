from fastapi import FastAPI

app = FastAPI()

# dg status_code = angka
@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

# lbh mudah dg fastapi status berisi kode jd tinggal panggil
from fastapi import status
@app.post("/withstatus/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}

# WE CAN CHANGE STATUS CODE, 
# in some cases you need to return a different status code than the default.
from fastapi import Response
tasks = {"foo": "Listen to the Bar Fighters"}


@app.put("/get-or-create-task/{task_id}", status_code=200)
def get_or_create_task(task_id: str, response: Response):
    # jika datanya tdk ada maka harus create a new data dg status code 201
    if task_id not in tasks:
        tasks[task_id] = "This didn't exist before"
        response.status_code = status.HTTP_201_CREATED
    return tasks[task_id]