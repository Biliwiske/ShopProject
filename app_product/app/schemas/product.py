from sqlalchemy import Column, String, DateTime, Float
from sqlalchemy.dialects.postgresql import UUID
from app.schemas.base_schema import Base


class Product(Base):
    __tablename__ = 'product'

    product_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    order_id = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)
