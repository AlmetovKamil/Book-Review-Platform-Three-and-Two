from pydantic import BaseModel


class Review(BaseModel):
    username: str = ""
    rating: float
    review: str
