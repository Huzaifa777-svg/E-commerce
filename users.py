from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models.user import User, UserCreate, UserRead
from core.db import get_session
from core.hashing import hash_password, verify_password
from core.jwt_handler import create_access_token

router = APIRouter()

@router.post("/signup", response_model=UserRead)
def signup(user: UserCreate, session: Session = Depends(get_session)):
    db_user = User(username=user.username, email=user.email, password=hash_password(user.password))
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@router.post("/login")
def login(user: UserCreate, session: Session = Depends(get_session)):
    db_user = session.exec(select(User).where(User.email == user.email)).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}
