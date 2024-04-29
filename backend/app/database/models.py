from .database import Base
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    favorite_books = relationship("FavoriteBook", back_populates="user")
    book_reviews = relationship("UserBookReview", back_populates="user")


class UserCreate(BaseModel):
    name: str


class FavoriteBook(Base):
    __tablename__ = "favorite_books"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(String)

    user = relationship("User", back_populates="favorite_books")


class UserBookReview(Base):
    __tablename__ = "user_book_reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(String)
    review = Column(String)
    rating = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="book_reviews")
