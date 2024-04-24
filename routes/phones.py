from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import Session, joinedload
from functions.phones import get_phones, create_phones, update_phones, delete_phones
from models.phones import Phones
from routes.login import get_current_active_user
from schemas.phones import CreatePhone, UpdatePhone
from schemas.users import CreateUser
from db import database

phone_router = APIRouter(
    prefix="/Phones",
    tags=["Phones operation"]
)


@phone_router.get('/get_random')
def get_random_phones(db: Session = Depends(database)):
    return db.query(Phones).options(joinedload(Phones.files)).order_by(func.random()).all()


@phone_router.get('/get_most_view')
def get_most_view_phone(db: Session = Depends(database)):
    most_viewed_phone = db.query(Phones).order_by(Phones.view.desc()).all()
    return most_viewed_phone


@phone_router.get('/get_most_like')
def get_most_likes_phone(db: Session = Depends(database)):
    return db.query(Phones).order_by(Phones.favorites.desc()).all()


@phone_router.get('/get')
def get_phone(ident: int = 0, brend: str = None, ram: int = 0, rom: int = 0, price: int = 0, page: int = 1,
              limit: int = 25, db: Session = Depends(database)):
    return get_phones(ident, brend, ram, rom, price, page, limit, db)


@phone_router.post('/create')
def create_phone(forms: List[CreatePhone], db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    create_phones(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@phone_router.put("/update")
def update_phone(forms: List[UpdatePhone], db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    update_phones(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@phone_router.delete("/delete")
def delete_phone(ident: int = 0, db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    delete_phones(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
