from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from models.order import Order
from core.db import get_session

router = APIRouter()

@router.post("/")
def create_order(order: Order, session: Session = Depends(get_session)):
    session.add(order)
    session.commit()
    session.refresh(order)
    return order

@router.get("/{user_id}")
def user_orders(user_id: int, session: Session = Depends(get_session)):
    return session.exec(select(Order).where(Order.user_id == user_id)).all()

@router.patch("/{order_id}/status")
def update_status(order_id: int, status: str, session: Session = Depends(get_session)):
    order = session.get(Order, order_id)
    if order:
        order.status = status
        session.commit()
        return {"message": "Order status updated"}
    return {"message": "Order not found"}
