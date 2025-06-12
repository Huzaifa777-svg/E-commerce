from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from models.cart import CartItem
from core.db import get_session

router = APIRouter()

@router.post("/")
def add_to_cart(item: CartItem, session: Session = Depends(get_session)):
    session.add(item)
    session.commit()
    return item

@router.get("/{user_id}")
def get_cart(user_id: int, session: Session = Depends(get_session)):
    return session.exec(select(CartItem).where(CartItem.user_id == user_id)).all()
