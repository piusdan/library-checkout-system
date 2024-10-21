from fastapi import FastAPI
from .routers import author, book, checkout
from .database import engine

app = FastAPI()

# Include the routers
app.include_router(author.router)
app.include_router(book.router)
app.include_router(checkout.router)

# Create the database tables
def create_tables():
    from .models import author, book, checkout
    author.Base.metadata.create_all(bind=engine)
    book.Base.metadata.create_all(bind=engine)
    checkout.Base.metadata.create_all(bind=engine)

create_tables()