from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import item_service
from schemas.item import ItemSchemaAdd
from services.item import ItemService

router = APIRouter(
    prefix="/items",
    tags=["Items"],
)


@router.post("")
async def add_item(
    item: ItemSchemaAdd,
    item_service: Annotated[ItemService, Depends(item_service)],
):
    item_id = await item_service.add_item(item)
    return {"item_id": item_id}


@router.get("")
async def get_stocks(
    item_service: Annotated[ItemService, Depends(item_service)],
):
    tasks = await item_service.get_items()
    return tasks
