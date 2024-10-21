# File: /library-checkout-system/library-checkout-system/app/routers/__init__.py

# This file is the initialization file for the `routers` package.

from fastapi import APIRouter

from . import author, book, checkout

router = APIRouter()

router.include_router(author.router, prefix="/authors", tags=["authors"])
router.include_router(book.router, prefix="/books", tags=["books"])
router.include_router(checkout.router, prefix="/checkouts", tags=["checkouts"])