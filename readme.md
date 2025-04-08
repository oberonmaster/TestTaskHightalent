# Restaurant Booking API

REST API сервис для бронирования столиков в ресторане. Построен на Django + DRF, использует PostgreSQL и обернут в Docker.

## Возможности

- Управление столами: создать, просмотреть, удалить.
- Управление бронями: создать, просмотреть, удалить.
- Проверка на пересечение броней по времени.
- Swagger-документация.
- Docker + PostgreSQL + Gunicorn.

## Быстрый старт

### 1. Клонируй проект

git clone https://github.com/yourname/restaurant-booking-api.git
cd restaurant-booking-api

### 2. Собери и запусти контейнеры

docker-compose up --build

Сервис будет доступен по адресу: http://localhost:8000

### 3. Swagger-документация

http://localhost:8000/swagger/
### 4. Admin panel

http://localhost:8000/admin/

### Создать суперпользователя:

docker-compose exec web python manage.py createsuperuser