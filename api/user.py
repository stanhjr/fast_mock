import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import user_service
from auth.permissions import PermissionsRouter
from models import User
from schemas.user import UserSchemaAdd, UserSchemaLogin, UserSchema, Token
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


@router.post("/login/", response_model=Token)
async def login(
    user: UserSchemaLogin,
    user_service: Annotated[UserService, Depends(user_service)],
):
    user = await user_service.check_password(user)
    return user


@router.delete("/{user_id}")
async def delete_user(
    user_id: uuid.UUID,
    user_service: Annotated[UserService, Depends(user_service)],
):
    user = await user_service.delete_user(user_id=user_id)
    return user


@router.get('/me', response_model=UserSchema)
def user_me(
        current_user: User = Depends(PermissionsRouter(("redf",)))
):
    return current_user
