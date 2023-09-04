from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import category_service
from schemas.category import CategorySchemaAdd
from services.category import CategoryService

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post("")
async def add_category(
    category: CategorySchemaAdd,
    category_service: Annotated[CategoryService, Depends(category_service)],
):
    category_id = await category_service.add_category(category)
    return {"category_id": category_id}


@router.get("")
async def get_categories(
    category_service: Annotated[CategoryService, Depends(category_service)],
):
    categories = await category_service.get_categories()
    return categories
