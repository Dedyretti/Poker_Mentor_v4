FROM python:3.11-slim

WORKDIR /app

# Копируем requirements.txt
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем папку poker_mentor
COPY poker_mentor/ ./poker_mentor/

# Устанавливаем переменные окружения
ENV PORT=8080

# Запускаем приложение
CMD ["python", "poker_mentor/bot/webhook_server.py"]