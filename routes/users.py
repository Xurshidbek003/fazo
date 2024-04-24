from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from functions.users import get_users, create_user, update_user, delete_user, create_admin
from routes.login import get_current_active_user
from schemas.users import CreateUser, UpdateUser, CreateGeneralUser
from db import database

users_router = APIRouter(
    prefix="/Users",
    tags=["Users operation"]
)


@users_router.get('/get')
def get(db: Session = Depends(database),
        current_user: CreateUser = Depends(get_current_active_user)):
    return get_users(db, current_user)


@users_router.get('/get_own')
def get_own(current_user: CreateUser = Depends(get_current_active_user)):
    return current_user


@users_router.post('/create')
def create_admins(form: CreateUser, db: Session = Depends(database),
                  current_user: CreateUser = Depends(get_current_active_user)):
    create_admin(form, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@users_router.post('/sign_up')
def create_users(form: CreateGeneralUser, db: Session = Depends(database)):
    create_user(form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@users_router.put("/update")
def update_users(form: UpdateUser, db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    update_user(form, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@users_router.delete("/delete")
def delete_users(db: Session = Depends(database),
                current_user: CreateUser = Depends(get_current_active_user)):
    delete_user(db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
