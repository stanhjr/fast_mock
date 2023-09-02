import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import user_service
from schemas.user import UserSchemaAdd, UserSchemaLogin
from services.user import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("")
async def add_user(
    user: UserSchemaAdd,
    user_service: Annotated[UserService, Depends(user_service)],
):
    user_id = await user_service.add_user(user)
    return {"user_id": user_id}


@router.get("")
async def get_users(
    user_service: Annotated[UserService, Depends(user_service)],
):
    users = await user_service.get_users()
    return users


@router.post("/login/")
async def login(
    user: UserSchemaLogin,
    user_service: Annotated[UserService, Depends(user_service)],
):
    user = await user_service.check_password(user)
    return user
