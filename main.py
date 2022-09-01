import time

from fastapi import FastAPI, Request

app = FastAPI()

# create middleware, every request must melalui middleware berupa func add_process_time_header
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    # lanjutkan ke func berikutnya yaitu request yg merupakan fastapi Request
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
