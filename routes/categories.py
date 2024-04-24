from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import database
from functions.categories import create_category, update_category, delete_category
from models.categories import Categories
from routes.login import get_current_user
from schemas.categories import CreateCategories, UpdateCategories
from schemas.users import CreateUser

category_router = APIRouter(
    prefix="/Categories",
    tags=["Categories operations"]
)


@category_router.post("/create")
def create_categories(forms: List[CreateCategories], db: Session = Depends(database),
                      current_user: CreateUser = Depends(get_current_user)):
    create_category(forms, db, current_user)
    raise HTTPException(200, "Amaliyot muvaffaqiyatli amalga oshirildi !!!")


@category_router.get("/get")
def get_categories(db: Session = Depends(database)):
    return db.query(Categories).all()


@category_router.put("/update")
def update_categories(forms: List[UpdateCategories], db: Session = Depends(database),
                      current_user: CreateUser = Depends(get_current_user)):
    update_category(forms, db, current_user)
    raise HTTPException(200, "Amaliyot muvaffaqiyatli amalga oshirildi !!!")


@category_router.delete("/delete")
def delete_categories(idents: List[int], db: Session = Depends(database),
                      current_user: CreateUser = Depends(get_current_user)):
    delete_category(db, idents, current_user)
    raise HTTPException(200, "Amaliyot muvaffaqiyatli amalga oshirildi !!!")
