from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# MULITPLE MODELS
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

# Pydantic's .dict()
# pydantic punya model .dict() yg akan mengembalikan suatu data model. contoh
user_in = UserIn(username="john", password="secret", email="john.doe@example.com")
# kita ambil dict() dari user_in diatas, merupakan dict bkn objek data model pydantic
user_dict = user_in.dict()
print(user_dict)
print(type(user_dict))

# Unwrapping a dict
"""
If we take a dict like user_dict and pass it to a function (or class) with **user_dict, Python will "unwrap" it.
It will pass the keys and values of the user_dict directly as key-value arguments.
kode dibawah ini sama saja (cara1==cara2)

"""
cara1= UserInDB(
    username="john",
    hashed_password="secret",
    email="john.doe@example.com",
    full_name=None,
)
# cara2 = UserInDB(**user_dict) # error karena pada data model UserIn tidak terdpt atribut hashed_password adanya password
# print(cara2)
cara3 = UserInDB(
    username = user_dict["username"],
    hashed_password = user_dict["password"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
)
print(cara1)
print(cara3)

# # # A Pydantic model from the contents of another
# # # got user_dict from user_in.dict()
# user_dict = user_in.dict()
# # UserInDB(**user_dict)# this will error cause didnt have hashed_password but have password attribut
# # # kode diatas akan == kode dibawah ini
# # UserInDB(**user_in.dict())# this will error cause didnt have hashed_password but have password attribut
# # # because user_in.dict() is a dict, and then we make Python "unwrap" it by passing it to UserInDB prepended with **
# # # So, we get a Pydantic model from the data in another Pydantic model.

# Unwrapping a dict and extra keywords
# adding the extra keyword argument hashed_password=hashed_password on user_dict (because user_dict didnt have hashed_password but have password)
unwrapping1 = UserInDB(**user_in.dict(), hashed_password=fake_password_hasher(user_dict["password"]))
print(unwrapping1)
# kode diatas akan sama sprti brkt
unwrapping2 = UserInDB(
    username = user_dict["username"],
    password = user_dict["password"],
    email = user_dict["email"],
    full_name = user_dict["full_name"],
    hashed_password = fake_password_hasher(user_dict["password"]),
)
print(unwrapping2)

# Reduce duplication
# code duplication increments the chances of bugs, security issues, code desynchronization issues (when you update in one place but not in the others), etc.
# yg duplikasi pd kasus data model adlh atribut username, email & fullname diulangi terus menerus untuk itu kita gunakan konsep inheritance pd data model response
class UserBase2(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

# inheritance ke UserBase2, ditambah atribut password
class UserIn2(UserBase2):
    password: str

# inheritance ke UserBase2
class UserOut2(UserBase2):
    pass

# inheritance ke UserBase2,, ditambah atribut hashed_password
class UserInDB2(UserBase2):
    hashed_password: str


def fake_password_hasher2(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user2(user_in: UserIn2):
    hashed_password = fake_password_hasher2(user_in.password)
    user_in_db = UserInDB2(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user2/", response_model=UserOut2)
async def create_user(user_in: UserIn2):
    user_saved = fake_save_user2(user_in)
    return user_saved

# Union or anyOf
# can declare a response to be the Union of two types, that means, that the response would be any of the two. use anyOf on openapi
from typing import Union
class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    # INI
    type = "car"


class PlaneItem(BaseItem):
    # INI
    type = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}

# INI OPENAPI. we pass Union[PlaneItem, CarItem] as the value of the argument response_model
# DI PYTHON 3.10 KITA TETAP MEMAKAI UNION KARENA JIKA response_model=PlaneItem | CarItem AKAN MENYEBABKAN ERROR
@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: int):
    return items[item_id]


# List of models
# can declare responses of lists of objects
# use the standard Python typing.List (or just list in Python 3.9 and above)
class Item(BaseModel):
    name: str
    description: str


items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/items/", response_model=list[Item])
async def read_items():
    return items

# Response with arbitrary dict
# can also declare a response using a plain arbitrary dict, declaring just the type of the keys and values, without using a Pydantic model
# useful if you don't know the valid field/attribute names (that would be needed for a Pydantic model) beforehand.
# can use typing.Dict (or just dict in Python 3.9 and above)
@app.get("/keyword-weights/", response_model=dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}