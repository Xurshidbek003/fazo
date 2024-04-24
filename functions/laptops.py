from sqlalchemy.orm import joinedload

from models.categories import Categories
from utils.db_operations import get_in_db, save_in_db
from utils.pagination import pagination
from models.laptops import Laptops
from fastapi import HTTPException


def get_laptop(ident, brend, ram, rom, price, page, limit, db):
    if ident > 0:
        ident_filter = Laptops.id == ident
        db.query(Laptops).filter(Laptops.id == ident).update({
            Laptops.view: Laptops.view + 1
        })
        db.commit()
    else:
        ident_filter = Laptops.id > 0
    if brend:
        search_formatted = "%{}%".format(brend)
        brend_filter = Laptops.brend.like(search_formatted)
    else:
        brend_filter = Laptops.id > 0
    if price > 0:
        price_filter = Laptops.price < price
    else:
        price_filter = Laptops.id > 0
    if ram > 0:
        ram_filter = Laptops.ram == ram
    else:
        ram_filter = Laptops.id > 0
    if rom > 0:
        rom_filter = Laptops.rom == rom
    else:
        rom_filter = Laptops.id > 0

    items = db.query(Laptops).options(joinedload(Laptops.files)).filter(ident_filter, brend_filter,
                                                                        price_filter, ram_filter, rom_filter).order_by(Laptops.id.desc())

    return pagination(items, page, limit)


def create_laptop(forms, db, user):
    if user.role == "admin":
        for form in forms:
            get_in_db(db, Categories, form.category_id)
            new_item_db = Laptops(
                category_id=form.category_id,
                name=form.name,
                brend=form.brend,
                model=form.model,
                processor=form.processor,
                ram=form.ram,
                rom=form.rom,
                rom_type=form.rom_type,
                color=form.color,
                screen_diagonal=form.screen_diagonal,
                screen_refresh=form.screen_refresh,
                videocard=form.videocard,
                cores=form.cores,
                weight=form.weight,
                country=form.country,
                year=form.year,
                price=form.price,
                discount=form.discount,
                discount_price=form.price - (form.price*form.discount)/100,
                discount_time=form.discount_time,
                count=form.count,
                source_name="laptop",
                view=0,
                favorites=0
            )
            save_in_db(db, new_item_db)

    else:
        raise HTTPException(400, " Error !!!")


def update_laptop(forms, db, user):
    if user.role == "admin":
        for form in forms:
            get_in_db(db, Laptops, form.ident)
            get_in_db(db, Categories, form.category_id)
            db.query(Laptops).filter(Laptops.id == form.ident).update({
                Laptops.category_id: form.category_id,
                Laptops.name: form.name,
                Laptops.brend: form.brend,
                Laptops.model: form.model,
                Laptops.processor: form.processor,
                Laptops.ram: form.ram,
                Laptops.rom: form.rom,
                Laptops.rom_type: form.rom_type,
                Laptops.color: form.color,
                Laptops.screen_diagonal: form.screen_diagonal,
                Laptops.screen_refresh: form.screen_refresh,
                Laptops.videocard: form.videocard,
                Laptops.cores: form.cores,
                Laptops.year: form.year,
                Laptops.country: form.country,
                Laptops.weight: form.weight,
                Laptops.price: form.price,
                Laptops.discount: form.discount,
                Laptops.discount_price: form.price - (form.price*form.discount)/100,
                Laptops.discount_time: form.discount_time,
                Laptops.count: form.count,
                Laptops.source_name: "laptop",
                Laptops.view: 0,
                Laptops.favorites: 0
            })
        db.commit()
    else:
        raise HTTPException(400, " Error !!!")


def delete_laptop(ident, db, user):
    if user.role == "admin":
        get_in_db(db, Laptops, ident)
        db.query(Laptops).filter(Laptops.id == ident).delete()
        db.commit()
    else:
        raise HTTPException(400, " Error !!!")
