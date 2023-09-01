from enum import Enum


class UserRoleEnum(str, Enum):
    supplier = "supplier"
    provider = "provider"
    warehouse_worker = "warehouse_worker"
    super_admin = "super_admin"
    shop_worker = "shop_worker"
    other = "other"


class PlaceTypeEnum(str, Enum):
    prime = "prime"
    local = "local"
    shop = "shop"


class ShipmentStatusEnum(str, Enum):
    on_the_way = "on_the_way"
    in_stock = "in_stock"


class OrderStatusEnum(str, Enum):
    to_stock = "to_stock"
    to_shop = "to_shop"
