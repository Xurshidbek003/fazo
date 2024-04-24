from fastapi import FastAPI

from routes.laptops import laptop_router
from routes.phones import phone_router
from routes.categories import category_router
from routes.tablets import tablet_router
from routes.users import users_router
from routes.login import login_router
from routes.files import files_router
from routes.likes import likes_router
from routes.carts import cart_router
from routes.buys import buy_router
from routes.main_page import main_router


app = FastAPI(docs_url='/')

app.include_router(main_router)
app.include_router(category_router)
app.include_router(laptop_router)
app.include_router(phone_router)
app.include_router(tablet_router)
app.include_router(files_router)
app.include_router(likes_router)
app.include_router(cart_router)
app.include_router(buy_router)
app.include_router(users_router)
app.include_router(login_router)
