import asyncio
from fastapi import FastAPI
from app import rabbitmq
from app.endpoints.product_router import product_router

app = FastAPI(title='Service')

app.include_router(product_router, prefix='/api')

@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(rabbitmq.consume(loop))