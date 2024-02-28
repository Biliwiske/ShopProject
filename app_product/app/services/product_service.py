from uuid import UUID, uuid4
from fastapi import Depends
from datetime import datetime

from app.models.product import Product
from app.repositories.db_product_repo import ProductRepo


class ProductService:
    order_repo: ProductRepo

    def __init__(self, product_repo: ProductRepo = Depends(ProductRepo)) -> None:
        self.product_repo = product_repo

    def get_product(self) -> list[Product]:
        return self.product_repo.get_product()

    def create_product(self, order_id: UUID, name: str, brand: str, price: str) -> Product:
        product = Product(product_id=uuid4(), order_id=order_id, name=name, brand=brand, price=price, created_at = datetime.utcnow())
        return self.product_repo.create_product(product)

    def delete_product(self, product_id: UUID) -> None:
        return self.product_repo.delete_product_by_id(product_id)
