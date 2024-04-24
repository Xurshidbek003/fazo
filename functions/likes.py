from utils.db_operations import get_in_db, save_in_db
from models.laptops import Laptops
from models.likes import Likes
from models.tablets import Tablets
from models.phones import Phones
from fastapi import HTTPException


def create_likes(form, db, user):
    if (form.source == "laptop" and db.query(Laptops).filter(form.source_id == Laptops.id).first() is None) or\
            (form.source == "phone" and db.query(Phones).filter(form.source_id == Phones.id).first() is None) or\
            (form.source == "tablet" and db.query(Tablets).filter(form.source_id == Tablets.id).first() is None):
        raise HTTPException(400, "Bunday mahsulot mavjud emas !!! ")

    likes = db.query(Likes).filter(
        Likes.user_id == user.id,
        Likes.source == form.source,
        Likes.source_id == form.source_id).first()

    if likes is not None:
        raise HTTPException(400, "Bunday mahsulot saralanganlarda mavjud !!!")

    new_item_db = Likes(
        user_id=user.id,
        source=form.source,
        source_id=form.source_id
    )
    save_in_db(db, new_item_db)

    if db.query(Laptops).filter(Laptops.id == form.source_id, Laptops.source_name == form.source):
        db.query(Laptops).filter(Laptops.id == form.source_id, Laptops.source_name == form.source).update({
            Laptops.favorites: Laptops.favorites + 1
        })
        db.commit()
    if db.query(Phones).filter(Phones.id == form.source_id, Phones.source_name == form.source):
        db.query(Phones).filter(Phones.id == form.source_id, Phones.source_name == form.source).update({
            Phones.favorites: Phones.favorites + 1
        })
        db.commit()
    if db.query(Tablets).filter(Tablets.id == form.source_id, Tablets.source_name == form.source):
        db.query(Tablets).filter(Tablets.id == form.source_id, Tablets.source_name == form.source).update({
            Tablets.favorites: Tablets.favorites + 1
        })
        db.commit()


def delete_likes(delete_all, ident, user, db):
    if delete_all:
        likes = db.query(Likes).all()
        for like in likes:
            if user.id == like.user_id:
                db.query(Likes).filter(Likes.id == like.id).delete()
                db.commit()
    elif db.query(Likes).filter(Likes.user_id == user.id):
        get_in_db(db, Likes, ident)
        db.query(Likes).filter(Likes.id == ident, Likes.user_id == user.id).delete()
        db.commit()
    else:
        raise HTTPException(400, " Bunday mahsulot saralanganlarda mavjud emas !!!")




