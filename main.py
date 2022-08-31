from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
# username & password didpt dari input form sehingga bertipe Form()
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
