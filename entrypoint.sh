#!/bin/sh
set -e

# Ожидание, пока база данных не станет доступной
/app/wait-for-db.sh db 5432

# Применяем миграции
python manage.py migrate

# Загружаем фикстуру (articles_4.json)
python manage.py loaddata articles_4.json

# Создаем суперпользователя, если его нет
python /app/create_admin.py

# Запускаем сервер Django
python manage.py runserver 0.0.0.0:8000
