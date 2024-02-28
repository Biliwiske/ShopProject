import enum
from uuid import UUID
from datetime import datetime
from pydantic import ConfigDict, BaseModel
from typing import Optional


class OrderStatus(enum.Enum):
    CREATE = 'create'
    PAID = 'paid'
    DELIVERING = 'delivering'
    DELIVERED = 'delivered'
    DONE = 'done'
    CANCELLED = 'cancelled'


class Order(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    order_id: UUID
    status: OrderStatus
    address_info: str
    customer_info: str
    create_date: datetime
    completion_date: Optional[datetime] = None
    order_info: str


class CreateOrderRequest(BaseModel):
    address_info: str
    customer_info: str
    order_info: str
