FROM python:3.10-slim

# Обновляем пакеты и устанавливаем netcat-openbsd для поддержки команды nc
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект, включая wait-for-db.sh и entrypoint.sh (если он используется)
COPY . .

# Делаем скрипты исполняемыми
RUN chmod +x /app/wait-for-db.sh && chmod +x /app/entrypoint.sh

# Открываем порт 8000 для Django
EXPOSE 8000

# Запускаем entrypoint-скрипт, который сначала ожидает базу, потом выполняет миграции, загрузку фикстуры, создание суперпользователя и запускает сервер
CMD ["sh", "-c", "/app/entrypoint.sh"]
