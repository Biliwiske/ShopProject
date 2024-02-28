from datetime import datetime
from uuid import UUID

from pydantic import ConfigDict, BaseModel


class Product(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_id: UUID
    order_id: UUID
    name: str
    brand: str
    price: float
    created_at: datetime


class CreateProductRequest(BaseModel):
    order_id: UUID
    name: str
    brand: str
    price: float
