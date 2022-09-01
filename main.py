from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# security kali ini kita memakai OAuth2
"""
The oauth2_scheme variable is an instance of OAuth2PasswordBearer, but it is also a "callable".
It could be called as oauth2_scheme(some, parameters) jd bisa memakai Depends
"""
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
# token as a str
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
