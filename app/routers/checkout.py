from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.checkout import CheckoutCreate, CheckoutUpdate
from ..models.checkout import Checkout

router = APIRouter()


@router.post("/checkouts", response_model=Checkout)
def create_checkout(checkout: CheckoutCreate, db: Session = Depends(get_db)):
    new_checkout = Checkout(**checkout.dict())
    db.add(new_checkout)
    db.commit()
    db.refresh(new_checkout)
    return new_checkout


@router.get("/checkouts/{checkout_id}", response_model=Checkout)
def read_checkout(checkout_id: int, db: Session = Depends(get_db)):
    checkout = db.query(Checkout).filter(Checkout.id == checkout_id).first()
    return checkout


@router.put("/checkouts/{checkout_id}", response_model=Checkout)
def update_checkout(checkout_id: int, checkout: CheckoutUpdate, db: Session = Depends(get_db)):
    db_checkout = db.query(Checkout).filter(Checkout.id == checkout_id).first()
    for field, value in checkout.dict().items():
        setattr(db_checkout, field, value)
    db.commit()
    db.refresh(db_checkout)
    return db_checkout


@router.delete("/checkouts/{checkout_id}")
def delete_checkout(checkout_id: int, db: Session = Depends(get_db)):
    checkout = db.query(Checkout).filter(Checkout.id == checkout_id).first()
    db.delete(checkout)
    db.commit()
    return {"message": "Checkout deleted successfully"}