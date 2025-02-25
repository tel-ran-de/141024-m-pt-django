# create_admin.py
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itg.settings')  # Задаем настройки Django

import django
django.setup()  # Инициализируем Django, чтобы можно было работать с моделями

from django.contrib.auth import get_user_model

User = get_user_model()

# Получаем данные для суперпользователя из переменных окружения или используем значения по умолчанию
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'adminpass')

# Проверяем, существует ли суперпользователь с заданным именем
if not User.objects.filter(username=username).exists():
    print("Creating superuser...")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print("Superuser already exists.")
