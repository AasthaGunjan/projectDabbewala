from enum import Enum
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class OrderStatus(str, Enum):
    PREPARING = "preparing"
    PICKED_UP = "picked_up"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_name: str
    delivery_address: str
    item: str
    status: OrderStatus = Field(default=OrderStatus.PREPARING)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now, sa_column_kwargs={"onupdate": datetime.now})

#Schema for creating a new order

class OrderCreate(SQLModel):
    customer_name: str
    delivery_address: str
    item: str

#Schema for updating an existing order's status

class OrderUpdate(SQLModel):
    status: Optional[OrderStatus] = None
    delivery_address: Optional[str] = None


class StatusLog(SQLModel):
    order_id: int
    old_status: OrderStatus
    new_status: OrderStatus
    changed_at: datetime = Field(default_factory=datetime.now)