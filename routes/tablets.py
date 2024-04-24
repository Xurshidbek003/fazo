from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.sql.expression import func
from sqlalchemy.orm import Session, joinedload
from functions.tablets import get_tablets, create_tablets, update_tablets, delete_tablets
from models.tablets import Tablets
from routes.login import get_current_active_user
from schemas.tablets import CreateTablet, UpdateTablet
from schemas.users import CreateUser
from db import database

tablet_router = APIRouter(
    prefix="/Tablets",
    tags=["Tablets operation"]
)


@tablet_router.get('/get_random')
def get_random_tablets(db: Session = Depends(database)):
    return db.query(Tablets).options(joinedload(Tablets.files)).order_by(func.random()).all()


@tablet_router.get('/get_most_view')
def get_most_view_tablet(db: Session = Depends(database)):
    most_viewed_tablet = db.query(Tablets).order_by(Tablets.view.desc()).all()
    return most_viewed_tablet


@tablet_router.get('/get_most_like')
def get_most_likes_tablet(db: Session = Depends(database)):
    return db.query(Tablets).order_by(Tablets.favorites.desc()).all()


@tablet_router.get('/get')
def get_tablet(ident: int = 0, brend: str = None, ram: int = 0, rom: int = 0,
               price: int = 0, page: int = 1, limit: int = 25,  db: Session = Depends(database)):
    return get_tablets(ident, brend, ram, rom, price, page, limit, db)


@tablet_router.post('/create')
def create_tablet(forms: List[CreateTablet], db: Session = Depends(database),
                  current_user: CreateUser = Depends(get_current_active_user)):
    create_tablets(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@tablet_router.put("/update")
def update_tablet(forms: List[UpdateTablet], db: Session = Depends(database),
                  current_user: CreateUser = Depends(get_current_active_user)):
    update_tablets(forms, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@tablet_router.delete("/delete")
def delete_tablet(ident: int = 0, db: Session = Depends(database),
                  current_user: CreateUser = Depends(get_current_active_user)):
    delete_tablets(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
