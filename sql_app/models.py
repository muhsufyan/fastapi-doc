from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# # Create SQLAlchemy models from the Base class, yg telah kita buat
from .database import Base

# class ini akan inherit dari class Base yg tlh kita buat untuk konek ke db
class User(Base):
    # nama tabel di db adlh users
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

# class ini akan inherit dari class Base yg tlh kita buat untuk konek ke db
class Item(Base):
    # nama tabel di db adlh items
    __tablename__ = "items"

    # ini menjd atribut/field di db
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # relasi
    owner = relationship("User", back_populates="items")
