from typing import List, Optional
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    availability: bool


class BookCreate(BookBase):
    author_id: int


class BookUpdate(BookBase):
    pass


class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True