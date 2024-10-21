from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.book import BookCreate, BookUpdate
from ..models.book import Book

router = APIRouter()


@router.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books


@router.get("/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return {"message": "Book not found"}
    return book


@router.post("/books")
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.put("/books/{book_id}")
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    existing_book = db.query(Book).filter(Book.id == book_id).first()
    if not existing_book:
        return {"message": "Book not found"}
    for field, value in book.dict().items():
        setattr(existing_book, field, value)
    db.commit()
    db.refresh(existing_book)
    return existing_book


@router.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return {"message": "Book not found"}
    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}