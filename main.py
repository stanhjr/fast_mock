import uvicorn
from fastapi import FastAPI

from api.routers import all_routers
from middlewares.unique_handle_middleware import HandleIntegrityErrorMiddleware

app = FastAPI(
    title="All stars"
)
app.add_middleware(HandleIntegrityErrorMiddleware)

for router in all_routers:
    app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
