from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, products, cart, order

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])

@app.get("/")
def root():
    return {"message": "Welcome to E-commerce API"}
from sqlmodel import SQLModel
from core.db import engine  # tumhara engine import yahan ho

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
