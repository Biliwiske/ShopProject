import datetime
from decimal import Decimal
from uuid import UUID

from app.models.product import Product
from typing import Optional

products: list[Product] = [
    Product(product_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'), order_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
             name='test_product_name_1', brand='test_brand1', price=Decimal(0.001), created_at=datetime.datetime),
    Product(product_id=UUID('45309954-8e3c-4635-8066-b342f634252c'), order_id=UUID('45309954-8e3c-4635-8066-b342f634252c'),
             name='test_product_name_2', brand='test_brand2', price=Decimal(0.014), created_at=datetime.datetime),
]


class ProductRepo():
    def __init__(self, clear: bool = False) -> None:
        if clear:
            products.clear()

    def get_product(self) -> list[Product]:
        return products

    def get_product_by_id(self, id: UUID) -> Product:
        for d in products:
            if d.product_id == id:
                return d

        raise KeyError

    def create_product(self, product: Product) -> Product:
        if len([d for d in products if d.product_id == product.product_id]) > 0:
            raise KeyError

        products.append(product)
        return product

    def delete_product(self, id: UUID) -> Optional[Product]:
        for i, product in enumerate(products):
            if product.product_id == id:
                deleted_product = products.pop(i)
                return deleted_product

        return None
