from sqlalchemy import Column, Integer, String
from .database import Base
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    favorite_books = relationship("FavoriteBook", back_populates="user")


class UserCreate(BaseModel):
    name: str


class FavoriteBook(Base):
    __tablename__= "favorite_books"

    id = Column(Integer, primary_key=True, index = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(String)

    user = relationship("User", back_populates="favorite_books")