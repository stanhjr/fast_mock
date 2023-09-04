from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import stock_service
from schemas.stock import StockSchemaAdd
from services.stock import StockService

router = APIRouter(
    prefix="/stocks",
    tags=["Stocks"],
)


@router.post("")
async def add_stock(
    stock: StockSchemaAdd,
    stock_service: Annotated[StockService, Depends(stock_service)],
):
    stock_id = await stock_service.add_stock(stock)
    return {"stock_id": stock_id}


@router.get("")
async def get_stocks(
    stock_service: Annotated[StockService, Depends(stock_service)],
):
    stocks = await stock_service.get_stocks()
    return stocks
