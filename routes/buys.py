from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from routes.login import get_current_active_user
from schemas.users import CreateUser
from models.carts import Carts
from utils.db_operations import get_in_db
from db import database

buy_router = APIRouter(
    prefix="/Buys",
    tags=["Buys operation"]
)


@buy_router.get("/get")
def get_buy(db: Session = Depends(database),
            current_user: CreateUser = Depends(get_current_active_user)):
    return db.query(Carts).filter(Carts.user_id == current_user.id, Carts.status == True).all()


@buy_router.put("/update")
def update_buy(ident, db: Session = Depends(database),
               current_user: CreateUser = Depends(get_current_active_user)):
    get_in_db(db, Carts, ident)

    if Carts.id == ident:
        if Carts.user_id != current_user.id:
            raise HTTPException(400, " Bunday mahsulot sizning savatchangizda mavjud emas !!!")

    db.query(Carts).filter(Carts.user_id == current_user.id).update({
        Carts.status: True
    })
    db.commit()
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
