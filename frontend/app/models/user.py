from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    username: str
    created_at: datetime
