from routes.login import get_password_hash
from utils.db_operations import save_in_db
from models.users import Users
from fastapi import HTTPException


def get_users(db, user):
    if user.role == "admin":
        return db.query(Users).all()
    else:
        raise HTTPException(400, " Error !!!")


def create_admin(form, db, user):
    if user.role == "admin":
        new_item_db = Users(
            name=form.name,
            username=form.username,
            phone_number=form.phone_number,
            role="admin",
            password=get_password_hash(form.password),
        )
        save_in_db(db, new_item_db)
    else:
        raise HTTPException(400, " Error !!!")


def create_user(form, db):
    new_item_db = Users(
        name=form.name,
        username=form.username,
        phone_number=form.phone_number,
        role="user",
        password=get_password_hash(form.password))
    save_in_db(db, new_item_db)


def update_user(form, db, user):
    db.query(Users).filter(Users.id == user.id).update({
        Users.name: form.name,
        Users.username: form.username,
        Users.password: get_password_hash(form.password),
        Users.role: user.role,
        Users.phone_number: form.phone_number
    })
    db.commit()


def delete_user(db, user):
    db.query(Users).filter(Users.id == user.id).delete()
    db.commit()
