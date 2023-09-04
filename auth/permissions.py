import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, Security
from starlette.status import HTTP_403_FORBIDDEN
from typing import Annotated

from api.dependencies import user_service
from schemas.user import UserSchemaAdd, UserSchemaLogin
from services.user import UserService

from models.user import User
from schemas.user import TokenPayload
from services.user import UserService

SECRET_KEY = "udfsdu6%$&(*Y9dHG(&ytdf987gFST*Sg897"
ALGORITHM = "HS256"
reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")


async def get_current_user(
        user_service: Annotated[UserService, Depends(user_service)],
        token: str = Security(reusable_oauth2)
) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    user = await user_service.get_user(user_id=token_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


class PermissionsRouter:
    def __init__(self, permissions: tuple):
        self.permissions = permissions

    def check_access(self, current_user: User):
        for permission in self.permissions:
            if permission == current_user.role:
                return current_user

        raise HTTPException(status_code=400, detail="The user doesn't have enough privileges")

    def __call__(self, user: User = Depends(get_current_user)):
        return self.check_access(current_user=user)
