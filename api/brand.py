import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import brand_service
from schemas.brand import BrandSchemaAdd
from services.brands import BrandService

router = APIRouter(
    prefix="/brands",
    tags=["Brands"],
)


@router.post("")
async def add_brand(
    brand: BrandSchemaAdd,
    brand_service: Annotated[BrandService, Depends(brand_service)],
):
    brand_id = await brand_service.add_brand(brand)
    return {"brand_id": brand_id}


@router.get("")
async def get_brands(
    brand_service: Annotated[BrandService, Depends(brand_service)],
):
    brands = await brand_service.get_brands()
    return brands


@router.delete("/{brand_id}")
async def delete_brand(
    brand_id: uuid.UUID,
    brand_service: Annotated[BrandService, Depends(brand_service)],
):
    brand = await brand_service.delete_brand(brand_id=brand_id)
    return brand
