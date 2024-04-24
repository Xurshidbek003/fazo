from models.carts import Carts
from utils.db_operations import get_in_db, save_in_db
from models.laptops import Laptops
from models.tablets import Tablets
from models.phones import Phones
from fastapi import HTTPException


def create_cart(form, db, user):
    if (db.query(Laptops).filter(Laptops.source_name == form.source).first() and db.query(Laptops).filter(Laptops.id == form.source_id).first() is None) or \
        (db.query(Tablets).filter(Tablets.source_name == form.source).first() and db.query(Tablets).filter(Tablets.id == form.source_id).first() is None) or \
            (db.query(Phones).filter(Phones.source_name == form.source).first() and db.query(Phones).filter(Phones.id == form.source_id).first() is None):
        raise HTTPException(400, " Ma'lumot topilmadi ")

    carts = db.query(Carts).filter(
        Carts.user_id == user.id,
        Carts.source == form.source,
        Carts.source_id == form.source_id).first()

    if carts is not None:
        db.query(Carts).filter(Carts.id == carts.id).update({
            Carts.product_count: Carts.product_count + 1
        })
        db.commit()
    else:
        new_item_db = Carts(
            user_id=user.id,
            source=form.source,
            source_id=form.source_id,
            product_count=1,
            status=False
        )
        save_in_db(db, new_item_db)


def delete_cart(ident, db, user):
    if Carts.user_id == user.id:
        get_in_db(db, Carts, ident)
        db.query(Carts).filter(Carts.user_id == user.id, Carts.id == ident).delete()
        db.commit()
    else:
        raise HTTPException(400, " Bunday mahsulot mavjud emas Sizda !!! ")







