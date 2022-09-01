from fastapi import FastAPI
# Use CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# list url yg dpt mengakses backend kita (list of allowed origins )
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

# tambahkan cors ke dlm middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
