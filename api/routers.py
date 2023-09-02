from api.brand import router as brands
from api.cetegory import router as categories
from api.group import router as group
from api.item import router as item
from api.sku import router as sku_s
from api.stock import router as stock
from api.user import router as user

all_routers = [
    user,
    brands,
    categories,
    sku_s,
    group,
    stock,
    item
]
