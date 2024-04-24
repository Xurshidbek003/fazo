from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import database
from models.laptops import Laptops
from models.tablets import Tablets
from models.phones import Phones
import random


main_router = APIRouter(
    prefix="/Main",
    tags=["Main operations"]
)


@main_router.get("/get")
def get_main_all_products(db: Session = Depends(database)):
    random_product = db.query(Laptops).all() + db.query(Phones).all() + db.query(Tablets).all()
    return random.sample(random_product, len(random_product))
