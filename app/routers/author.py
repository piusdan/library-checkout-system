from fastapi import APIRouter, HTTPException

from ..schemas.author import AuthorCreate, AuthorUpdate, Author
from ..models.author import Author as DBAuthor

router = APIRouter()


@router.post("/authors", response_model=Author)
def create_author(author: AuthorCreate):
    db_author = DBAuthor.create(**author.dict())
    return db_author


@router.get("/authors/{author_id}", response_model=Author)
def read_author(author_id: int):
    db_author = DBAuthor.get(author_id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@router.put("/authors/{author_id}", response_model=Author)
def update_author(author_id: int, author: AuthorUpdate):
    db_author = DBAuthor.get(author_id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    db_author.update(**author.dict(exclude_unset=True))
    return db_author


@router.delete("/authors/{author_id}")
def delete_author(author_id: int):
    db_author = DBAuthor.get(author_id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    db_author.delete()
    return {"message": "Author deleted"}