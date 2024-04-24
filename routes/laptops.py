from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import Session
from db import database
from functions.laptops import get_laptop, create_laptop, update_laptop, delete_laptop
from models.laptops import Laptops
from routes.login import get_current_active_user
from schemas.laptops import CreateLaptop, UpdateLaptop
from schemas.users import CreateUser
from sqlalchemy.orm import joinedload

laptop_router = APIRouter(
    prefix="/Laptop",
    tags=["Laptop operation"]
)


@laptop_router.get('/get_random')
def get_random_laptops(db: Session = Depends(database)):
    return db.query(Laptops).options(joinedload(Laptops.files)).order_by(func.random()).all()


@laptop_router.get('/get_most_view')
def get_most_view_laptop(db: Session = Depends(database)):
    most_viewed_laptop = db.query(Laptops).order_by(Laptops.view.desc()).all()
    return most_viewed_laptop


@laptop_router.get('/get_most_like')
def get_most_likes_laptop(db: Session = Depends(database)):
    return db.query(Laptops).order_by(Laptops.favorites.desc()).all()


@laptop_router.get('/get')
def get_laptops(ident: int = 0, brend: str = None, ram: int = 0, rom: int = 0, price: int = 0, page: int = 1,
                limit: int = 25, db: Session = Depends(database)):
    return get_laptop(ident, brend, ram, rom, price, page, limit, db)


@laptop_router.post('/create')
def create_laptops(forms: List[CreateLaptop], db: Session = Depends(database),
                   current_user: CreateUser = Depends(get_current_active_user)):
    create_laptop(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@laptop_router.put("/update")
def update_laptops(forms: List[UpdateLaptop], db: Session = Depends(database),
                   current_user: CreateUser = Depends(get_current_active_user)):
    update_laptop(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@laptop_router.delete("/delete")
def delete_laptops(ident: int = 0, db: Session = Depends(database),
                   current_user: CreateUser = Depends(get_current_active_user)):
    delete_laptop(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
