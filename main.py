from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

# HTTPException
# To return HTTP responses with errors to the client
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        # ID doesn't exist will catch as error in program and we treat as 404
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}

# Add custom headers
# ex token pd headers
@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}

"""
Let's say you have a custom exception UnicornException that you (or a library you use) might raise.

And you want to handle this exception globally with FastAPI.

You could add a custom exception handler with @app.exception_handler()
"""
from fastapi.responses import JSONResponse
from fastapi import Request

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )

"""
if you request /unicorns/yolo, the path operation will raise a UnicornException.

But it will be handled by the unicorn_exception_handler
will receive a clean error, with an HTTP status code of 418 and a JSON content
"""
@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}

# Override the default exception handlers
# Override request validation exceptions
"""
When a request contains invalid data, FastAPI internally raises a RequestValidationError.
And it also includes a default exception handler for it.

To override it, import the RequestValidationError and use it with @app.exception_handler(RequestValidationError) to decorate the exception handler.
The exception handler will receive a Request and the exception.
"""
# import this
from fastapi.exceptions import RequestValidationError

from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

# Override the HTTPException error handler
"""
can override the HTTPException handler.
For example, you could want to return a plain text response instead of JSON for these errors
"""
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

# /items/foo will error
@app.get("/overridereqvalidasi/Exception/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}

# RequestValidationError vs ValidationError
"""
RequestValidationError is a sub-class of Pydantic's ValidationError,
so if you use a Pydantic model in response_model, and your data has an error, you will see the error in your log.
but user see 500. shrsnya begitu karena jika response-nya adlh ValidationError itu jd bug
"""




# Use the RequestValidationError body
from fastapi.encoders import jsonable_encoder
from fastapi import status
from pydantic import BaseModel
"""
The RequestValidationError contains the body it received with invalid data.
You could use it while developing your app to log the body and debug it, return it to the user, etc.
"""
@app.exception_handler(RequestValidationError)
async def validation_exception_handler2(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        # INI
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )
class Item(BaseModel):
    title: str
    size: int


@app.post("/items/")
async def create_item(item: Item):
    return item

# Re-use FastAPI's exception handlers¶
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
# If you want to use the exception along with the same default exception handlers from FastAPI,
# You can import and re-use the default exception handlers from fastapi.exception_handlers
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"OMG! An HTTP error!: {repr(exc)}")
    # ini
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler3(request, exc):
    print(f"OMG! The client sent invalid data!: {exc}")
    # ini
    return await request_validation_exception_handler(request, exc)


@app.get("/re-use/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}