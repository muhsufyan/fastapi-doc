from fastapi import FastAPI
# OpenAPI URL
"""
By default, the OpenAPI schema is served at /openapi.json.
But you can configure it with the parameter openapi_url.
For example, to set it to be served at /api/v1/openapi.json
"""
# param openapi_url for doc openapi
app = FastAPI(openapi_url="/api/v1/openapi.json")


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]