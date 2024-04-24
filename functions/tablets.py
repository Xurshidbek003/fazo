from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models.categories import Categories
from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.tablets import Tablets


def get_tablets(ident, brend, ram, rom, price, page, limit, db):
    if ident > 0:
        ident_filter = Tablets.id == ident
        db.query(Tablets).filter(Tablets.id == ident).update({
            Tablets.view: Tablets.view + 1
        })
        db.commit()
    else:
        ident_filter = Tablets.id > 0
    if brend:
        search_formatted = "%{}%".format(brend)
        brend_filter = (Tablets.brend.like(search_formatted))
    else:
        brend_filter = Tablets.id > 0
    if ram > 0:
        ram_filter = Tablets.ram == ram
    else:
        ram_filter = Tablets.id > 0
    if rom > 0:
        rom_filter = Tablets.rom == ram
    else:
        rom_filter = Tablets.id > 0
    if price > 0:
        price_filter = Tablets.price == price
    else:
        price_filter = Tablets.id > 0

    items = db.query(Tablets).options(joinedload(Tablets.files)).filter(ident_filter, brend_filter, ram_filter, rom_filter, price_filter).order_by(Tablets.id.desc())
    return pagination(items, page, limit)


def create_tablets(forms, db, user):
    for form in forms:
        if user.role == "admin":
            get_in_db(db, Categories, form.category_id)
            new_item_db = Tablets(
                category_id=form.category_id,
                name=form.name,
                brend=form.brend,
                model=form.model,
                ram=form.ram,
                rom=form.rom,
                battery=form.battery,
                color=form.color,
                screen_diagonal=form.screen_diagonal,
                screen_refresh=form.screen_refresh,
                camera=form.camera,
                self_camera=form.self_camera,
                weight=form.weight,
                year=form.year,
                country=form.country,
                price=form.price,
                discount=form.discount,
                discount_price=form.price - (form.discount * form.price) / 100,
                discount_time=form.discount_time,
                count=form.count,
                source_name="tablet",
                view=0,
                favorites=0
            )
            save_in_db(db, new_item_db)
        else:
            raise HTTPException(400, " Error !!!")


def update_tablets(forms, db, user):
    for form in forms:
        if user.role == "admin":
            get_in_db(db, Tablets, form.ident)
            get_in_db(db, Categories, form.category_id)
            db.query(Tablets).filter(Tablets.id == form.ident).update({
                Tablets.category_id: form.category_id,
                Tablets.name: form.name,
                Tablets.brend: form.brend,
                Tablets.model: form.model,
                Tablets.ram: form.ram,
                Tablets.rom: form.rom,
                Tablets.battery: form.battery,
                Tablets.color: form.color,
                Tablets.screen_diagonal: form.screen_diagonal,
                Tablets.screen_refresh: form.screen_refresh,
                Tablets.camera: form.camera,
                Tablets.self_camera: form.self_camera,
                Tablets.weight: form.weight,
                Tablets.year: form.year,
                Tablets.country: form.country,
                Tablets.price: form.price,
                Tablets.discount: form.discount,
                Tablets.discount_price: form.price - (form.discount * form.price) / 100,
                Tablets.discount_time: form.discount_time,
                Tablets.count: form.count,
                Tablets.source_name: "tablet",
                Tablets.view: 0,
                Tablets.favorites: 0
            })
            db.commit()
        else:
            raise HTTPException(400, " Error !!! ")


def delete_tablets(db, idents, user):
    if user.role == "admin":
        for ident in idents:
            get_in_db(db, Tablets, ident)
            db.query(Tablets).filter(Tablets.id == ident).delete()
        db.commit()
    else:
        raise HTTPException(400, " Error !!!")
