from fastapi import FastAPI

# Metadata for API
description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    # Metadata for API
    title="ChimichangApp",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get("/metadata/API/items/")
async def read_items():
    return [{"name": "Katana"}]

# Metadata for tags

# Create metadata for tags. tags for users and items
tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]
# add additional metadata for the different tags used to group your path operations with the parameter openapi_tags
app = FastAPI(openapi_tags=tags_metadata)

# Use the tags parameter with your path operations (and APIRouters) to assign them to different tags
@app.get("/metadata/tags/users/", tags=["users"])
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]

# Use the tags parameter with your path operations (and APIRouters) to assign them to different tags
@app.get("/metadata/tags/items/", tags=["items"])
async def get_items():
    return [{"name": "wand"}, {"name": "flying broom"}]


# OpenAPI URL
"""
By default, the OpenAPI schema is served at /openapi.json.
But you can configure it with the parameter openapi_url.
For example, to set it to be served at /api/v1/openapi.json
"""

app = FastAPI(openapi_url="/api/v1/openapi.json")


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]