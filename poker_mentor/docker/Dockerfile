FROM python:3.11-slim

WORKDIR /app

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копирование requirements
COPY requirements/ /app/requirements/

# Установка Python зависимостей
RUN pip install --no-cache-dir -r requirements/base.txt

# Копирование исходного кода
COPY app/ /app/app/

# Команда по умолчанию
CMD ["python", "-m", "app.main"]