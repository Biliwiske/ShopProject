FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /app_product

# Установка зависимостей проекта
COPY ./app_product/requirements.txt /app_product/
RUN pip install --no-cache-dir --upgrade -r /app_product/requirements.txt

# Перенос проекта в образ
COPY ./app_product/app /app_product/app
COPY .env /app_product

# Копирование файлов alembic
COPY ./app_product/migration /app_product/migration
COPY ./app_product/alembic.ini /app_product/alembic.ini

EXPOSE 81

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 81"]