from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import sku_service
from schemas.sku import SkuSchemaAdd
from services.sku import SkuService

router = APIRouter(
    prefix="/sku",
    tags=["Sku"],
)


@router.post("")
async def add_sku(
    sku: SkuSchemaAdd,
    sku_service: Annotated[SkuService, Depends(sku_service)],
):
    sku_id = await sku_service.add_sku(sku)
    return {"sku_id": sku_id}


@router.get("")
async def get_sku_s(
    sku_service: Annotated[SkuService, Depends(sku_service)],
):
    sku_list = await sku_service.get_sku_list()
    return sku_list
