import traceback
from uuid import UUID
from sqlalchemy.orm import Session

from app.database import get_db_product
from app.models.product import Product
from app.schemas.product import Product as DBProduct


class ProductRepo():
    db: Session

    def __init__(self) -> None:
        self.db = next(get_db_product())

    def _map_to_model(self, product: DBProduct) -> Product:
        result = Product.from_orm(product)

        return result

    def _map_to_schema(self, product: Product) -> DBProduct:
        data = dict(product)
        result = DBProduct(**data)

        return result

    def get_product(self) -> list[Product]:
        products = []
        for d in self.db.query(DBProduct).all():
            products.append(self._map_to_model(d))

        return products

    def get_product_by_id(self, id: UUID) -> Product:
        product = self.db \
            .query(DBProduct) \
            .filter(DBProduct.product_id == id) \
            .first()

        if product == None:
            raise KeyError
        return self._map_to_model(product)

    def create_product(self, product: Product) -> Product:
        try:
            db_product = self._map_to_schema(product)
            self.db.add(db_product)
            self.db.commit()
            return self._map_to_model(db_product)
        except:
            traceback.print_exc()
            raise KeyError

    def delete_product_by_id(self, id: UUID) -> Product:
        try:
            # Find the order by its order_id
            product = self.db.query(DBProduct).filter(DBProduct.product_id == id).one()

            # If the order is found, map it to the model and commit the deletion
            if product:
                deleted_product = self._map_to_model(product)
                self.db.delete(product)
                self.db.commit()
                return deleted_product
            else:
                # Handle the case where no order is found
                raise ValueError(f"No order found with order_id {id}")
        except Exception as e:
            # Rollback any changes if there's an error
            self.db.rollback()
            # Re-raise the exception so it can be handled elsewhere
            raise e
