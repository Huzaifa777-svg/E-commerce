from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    is_admin: bool = False

class UserCreate(SQLModel):
    username: str
    email: str
    password: str

class UserRead(SQLModel):
    id: int
    username: str
    email: str
    is_admin: bool
