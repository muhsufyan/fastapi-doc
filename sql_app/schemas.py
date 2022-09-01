# DATA MODEL

# Jika memakai SQLAlchemy formatnya => name = Column(String) sedangkan untuk pydantic => name: str
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

# This Config class is used to provide configurations to Pydantic.
# In the Config class, set the attribute orm_mode = True
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

# This Config class is used to provide configurations to Pydantic.
# In the Config class, set the attribute orm_mode = True
    class Config:
        orm_mode = True
