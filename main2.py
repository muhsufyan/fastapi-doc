from fastapi import FastAPI
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