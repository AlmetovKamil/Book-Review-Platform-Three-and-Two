from typing import List, Optional
from pydantic import BaseModel

from app.models.genre import Genre


class Book(BaseModel):
    title: str
    author_name: str = ""
    rating: Optional[float] = None
    genre: Genre = Genre.fiction
    cover_link: str
    description: str = "Some long long long "
    reviews: List[str] = []
