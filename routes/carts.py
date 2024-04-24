from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session, joinedload
from functions.carts import create_cart, delete_cart
from models.carts import Carts
from routes.login import get_current_active_user
from schemas.carts import CreateCarts
from schemas.users import CreateUser
from db import database


cart_router = APIRouter(
    prefix="/cart",
    tags=["Cart operation"]
)


@cart_router.get('/get')
def get_cart(db: Session = Depends(database),
             current_user: CreateUser = Depends(get_current_active_user)):
    return db.query(Carts).options(joinedload(Carts.laptop), joinedload(Carts.phone),
                                   joinedload(Carts.tablet), joinedload(Carts.users)).filter(Carts.user_id == current_user.id).all()


@cart_router.post('/create')
def create_carts(form: CreateCarts = Depends(CreateCarts), db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    create_cart(form, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@cart_router.delete("/delete")
def delete_carts(ident: int = 0, db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    delete_cart(ident, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
