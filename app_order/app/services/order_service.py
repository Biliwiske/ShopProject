from uuid import UUID, uuid4
from fastapi import Depends
from datetime import datetime
import asyncio

from app.models.order import Order, OrderStatus
from app.rabbitmq import send_to_product_queue
from app.repositories.db_order_repo import OrderRepo


class OrderService():
    order_repo: OrderRepo
    def __init__(self, order_repo: OrderRepo = Depends(OrderRepo), ) -> None:
        self.order_repo = order_repo

    def get_order(self) -> list[Order]:
        return self.order_repo.get_order()

    def create_order(self, address_info: str, customer_info: str, order_info: str) -> Order:
        order = Order(order_id=uuid4(), status=OrderStatus.CREATE, address_info=address_info, customer_info=customer_info,
                      create_date=datetime.now(), completion_date=None, order_info=order_info)
        return self.order_repo.create_order(order)

    def paid_order(self, id: UUID) -> Order:
        order = self.order_repo.get_order_by_id(id)
        if order.status != (OrderStatus.CREATE):
            raise ValueError

        order.status = OrderStatus.PAID
        return self.order_repo.set_status(order)

    def delivering_order(self, id: UUID) -> Order:
        order = self.order_repo.get_order_by_id(id)
        if order.status != OrderStatus.PAID:
            raise ValueError

        order.status = OrderStatus.DELIVERING
        return self.order_repo.set_status(order)

    def delivered_order(self, id: UUID) -> Order:
        order = self.order_repo.get_order_by_id(id)
        if order.status != OrderStatus.DELIVERING:
            raise ValueError

        order.status = OrderStatus.DELIVERED
        return self.order_repo.set_status(order)

    def done_order(self, id: UUID) -> Order:
        order = self.order_repo.get_order_by_id(id)
        if order.status != OrderStatus.DELIVERED:
            raise ValueError

        order.status = OrderStatus.DONE
        order.completion_date = datetime.now()
        return self.order_repo.set_status(order)

    def cancel_order(self, id: UUID) -> Order:
        order = self.order_repo.get_order_by_id(id)
        if order.status != (OrderStatus.CREATE):
            raise ValueError

        order.status = OrderStatus.CANCELLED
        return self.order_repo.set_status(order)
