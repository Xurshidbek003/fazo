from fastapi import HTTPException
from models.categories import Categories
from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.phones import Phones
from sqlalchemy.orm import joinedload


def get_phones(ident, brend, ram, rom, price, page, limit, db):
    if ident > 0:
        ident_filter = Phones.id == ident
        db.query(Phones).filter(Phones.id == ident).update({
            Phones.view: Phones.view + 1
        })
        db.commit()
    else:
        ident_filter = Phones.id > 0

    if brend:
        search_formatted = "%{}%".format(brend)
        brend_filter = (Phones.brand.like(search_formatted))
    else:
        brend_filter = Phones.id > 0

    if ram > 0:
        ram_filter = Phones.ram == ram
    else:
        ram_filter = Phones.id > 0

    if rom > 0:
        rom_filter = Phones.rom == ram
    else:
        rom_filter = Phones.id > 0

    if price > 0:
        price_filter = Phones.price == price
    else:
        price_filter = Phones.id > 0

    items = db.query(Phones).options(joinedload(Phones.files)).filter(ident_filter, brend_filter, ram_filter, rom_filter, price_filter).order_by(
        Phones.id.desc())

    return pagination(items, page, limit)


def create_phones(forms, db, user):
    if user.role == "admin":
        for form in forms:
            get_in_db(db, Categories, form.category_id)
            new_item_db = Phones(
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
                source_name="phone",
                view=0,
                favorites=0
            )
            save_in_db(db, new_item_db)
    else:
        raise HTTPException(400, " Error !!!")


def update_phones(forms, db, user):
    for form in forms:
        if user.role == "admin":
            get_in_db(db, Phones, form.ident)
            get_in_db(db, Categories, form.category_id)
            db.query(Phones).filter(Phones.id == form.ident).update({
                Phones.category_id: form.category_id,
                Phones.name: form.name,
                Phones.brend: form.brend,
                Phones.model: form.model,
                Phones.ram: form.ram,
                Phones.rom: form.rom,
                Phones.battery: form.battery,
                Phones.color: form.color,
                Phones.screen_diagonal: form.screen_diagonal,
                Phones.screen_refresh: form.screen_refresh,
                Phones.camera: form.camera,
                Phones.self_camera: form.self_camera,
                Phones.weight: form.weight,
                Phones.year: form.year,
                Phones.country: form.country,
                Phones.price: form.price,
                Phones.discount: form.discount,
                Phones.discount_price: form.price - (form.discount * form.price) / 100,
                Phones.discount_time: form.discount_time,
                Phones.count: form.count,
                Phones.source_name: "phone",
                Phones.view: 0,
                Phones.favorites: 0
            })
            db.commit()
        else:
            raise HTTPException(400, " Error !!! ")


def delete_phones(db, idents, user):
    if user.role == "admin":
        for ident in idents:
            get_in_db(db, Phones, ident)
            db.query(Phones).filter(Phones.id == ident).delete()
        db.commit()
    else:
        raise HTTPException(400, " Error !!!")
