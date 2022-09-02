from fastapi import FastAPI
# Use StaticFiles
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# "Mount" a StaticFiles() instance in a specific path
# arti dr mount disini adlh adding a complete "independent" application in a specific path, that then takes care of handling all the sub-paths
"""
The first "/static" refers to the sub-path this "sub-application" will be "mounted" on
So, any path that starts with "/static" will be handled by it.

The directory="static" refers to the name of the directory that contains your static files.
The name="static" gives it a name that can be used internally by FastAPI.
"""
# kita harus buat folder static
app.mount("/static", StaticFiles(directory="static/"), name="static")
