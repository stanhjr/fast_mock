from api.brands import router as brands
from api.cetegory import router as categories
from api.sku import router as sku_s
from api.group import router as group

all_routers = [
    brands,
    categories,
    sku_s,
    group
]
