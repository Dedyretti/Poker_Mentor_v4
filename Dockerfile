FROM python:3.11-alpine

WORKDIR /app

# Устанавливаем системные зависимости для компиляции
RUN apk add --no-cache \
    gcc \
    g++ \
    musl-dev \
    linux-headers \
    libffi-dev \
    openssl-dev

# Копируем requirements
COPY requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Удаляем компиляторы (они больше не нужны)
RUN apk del gcc g++ musl-dev linux-headers

# Копируем код
COPY poker_mentor/ ./poker_mentor/

ENV PORT=8080
CMD ["python", "poker_mentor/bot/webhook_server.py"]