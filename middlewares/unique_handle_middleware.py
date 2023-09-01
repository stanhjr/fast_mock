from sqlalchemy.exc import IntegrityError, NoResultFound
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

from middlewares.utils import extract_unique_field_from_error


class HandleIntegrityErrorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except IntegrityError as e:
            print(e)

            if "unique" in str(e.orig).lower():
                unique_field = extract_unique_field_from_error(e)
                return JSONResponse(status_code=400, content=f"Field '{unique_field}' must be unique")

            return JSONResponse(status_code=400, content=f"IntegrityError something wrong")

        except NoResultFound as e:
            print(e)
            return JSONResponse(status_code=400, content=str(e))
