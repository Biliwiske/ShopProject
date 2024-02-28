from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException

from app.services.product_service import ProductService
from app.models.product import Product, CreateProductRequest

product_router = APIRouter(prefix='/product', tags=['Product'])


@product_router.get('/')
def get_product(product_service: ProductService = Depends(ProductService)) -> list[Product]:
    return product_service.get_product()


@product_router.post('/')
def add_order(
        product_info: CreateProductRequest,
        product_service: ProductService = Depends(ProductService)
) -> Product:
    try:
        product = product_service.create_product(product_info.order_id, product_info.name, product_info.brand,
                                                 product_info.price)
        return product.dict()
    except KeyError:
        raise HTTPException(400, f'Order with id={product_info.product_id} already exists')


@product_router.post('/{id}/delete')
def delete_order(id: UUID, product_service: ProductService = Depends(ProductService)) -> Product:
    try:
        product = product_service.delete_product(id)
        return product.dict()
    except KeyError:
        raise HTTPException(404, f'Product with id={id} not found')
