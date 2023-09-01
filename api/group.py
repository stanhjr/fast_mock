from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import group_service
from schemas.group import GroupSchemaAdd
from services.group import GroupService

router = APIRouter(
    prefix="/groups",
    tags=["Groups"],
)


@router.post("")
async def add_group(
    group: GroupSchemaAdd,
    group_service: Annotated[GroupService, Depends(group_service)],
):
    group_id = await group_service.add_group(group)
    return {"group_id": group_id}


@router.get("")
async def get_groups(
    group_service: Annotated[GroupService, Depends(group_service)],
):
    tasks = await group_service.get_groups()
    return tasks
