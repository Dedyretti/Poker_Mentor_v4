FROM python:3.11-slim

WORKDIR /app

# Устанавливаем только системные зависимости которые нужны
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY poker_mentor/requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем только нужные файлы
COPY poker_mentor/ .

CMD ["python", "bot/webhook_server.py"]