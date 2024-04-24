from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session, joinedload
from functions.likes import create_likes, delete_likes
from models.laptops import Laptops
from models.likes import Likes
from models.phones import Phones
from models.tablets import Tablets
from routes.login import get_current_active_user, get_current_user
from schemas.users import CreateUser
from schemas.likes import CreateLikes
from db import database

likes_router = APIRouter(
    prefix="/Likes",
    tags=["Likes operation"]
)


@likes_router.get('/get_source')
def get_source_like(db: Session = Depends(database),
                    current_user: CreateUser = Depends(get_current_active_user)):
    return db.query(Laptops).options(joinedload(Laptops.files)).filter(current_user.id == Likes.user_id,
                                                                       Laptops.id == Likes.source_id,
                                                                       Likes.source == Laptops.source_name).all() + \
        db.query(Tablets).options(joinedload(Tablets.files)).filter(current_user.id == Likes.user_id,
                                                                    Tablets.id == Likes.source_id,
                                                                    Likes.source == Tablets.source_name).all() + \
        db.query(Phones).options(joinedload(Phones.files)).filter(current_user.id == Likes.user_id,
                                                                  Phones.id == Likes.source_id,
                                                                  Likes.source == Phones.source_name).all()


@likes_router.get('/get')
def get_likes(db: Session = Depends(database),
              current_user: CreateUser = Depends(get_current_active_user)):
    return db.query(Likes).filter(Likes.user_id == current_user.id).all()


@likes_router.get('/get_count')
def get_likes_count(db: Session = Depends(database),
                    current_user: CreateUser = Depends(get_current_active_user)):
    return len(db.query(Likes).filter(Likes.user_id == current_user.id).all())


@likes_router.post('/create')
def create_like(form: CreateLikes = Depends(CreateLikes), db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    create_likes(form, db, current_user)
    raise HTTPException(200, "Amaliyot muvaffaqiyatli amalga oshirildi")


@likes_router.delete("/delete")
def delete_like(delete_all: bool = False, ident: int = 0, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_user)):
    delete_likes(delete_all, ident, current_user, db)
    raise HTTPException(200, "Amaliyot muvaffaqiyatli amalga oshirildi")
