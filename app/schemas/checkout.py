from datetime import date
from pydantic import BaseModel


class CheckoutBase(BaseModel):
    book_id: int
    checkout_date: date
    return_date: date


class CheckoutCreate(CheckoutBase):
    pass


class CheckoutUpdate(CheckoutBase):
    pass


class Checkout(CheckoutBase):
    id: int

    class Config:
        orm_mode = True