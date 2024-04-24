from utils.db_operations import save_in_db, get_in_db
from utils.pagination import pagination
from models.categories import Categories
from fastapi import HTTPException


def get_category(page, limit, db):
    items = db.query(Categories).all()
    return pagination(items, page, limit)


def create_category(forms, db, user):
    if user.role == "admin":
        for form in forms:
            new_item_db = Categories(
                name=form.name)
            save_in_db(db, new_item_db)
    else:
        raise HTTPException(400, " Error !!! ")


def update_category(forms, db, user):
    if user.role == "admin":
        for form in forms:
            get_in_db(db, Categories, form.ident)
            db.query(Categories).filter(Categories.id == form.ident).update({
                Categories.name: form.name
            })
        db.commit()
    else:
        raise HTTPException(400, " Error !!! ")


def delete_category(db, idents, user):
    if user.role == "admin":
        for ident in idents:
            get_in_db(db, Categories, ident)
            db.query(Categories).filter(Categories.id == ident).delete()
        db.commit()
    else:
        raise HTTPException(400, " Error !!!")



