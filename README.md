# fastapi-doc

## how to run
python -m venv virtualenv<br>
windows => .\virtualenv\Scripts\activate.bat<br>
update => virtualenv\Scripts\python.exe -m pip install --upgrade pip<br>
run => uvicorn app.main:app --reload<br>
* dimana app adlh root dir, main adlah file main.py & app adlah FastAPI()<br>
# note
di python 3.6, OR pd param func menggunakan union<br>
=> q: Union[str, None] = None<br>
sedangkan untuk 3.10<br>
=>  q: str | None = None

# Bigger Applications - Multiple Files
setiap folder akan memiliki __init__.py fungsinya agar code dlm folder dpt diimport oleh folder & file lainnya<br>
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   │   └── users.py     # "users" submodule, e.g. import app.routers.users
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import app.internal.admin