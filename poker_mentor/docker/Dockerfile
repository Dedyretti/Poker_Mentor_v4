FROM python:3.12-slim

WORKDIR /app

# Копируем зависимости сначала для кэширования
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Создаем переменную для порта (Railway сам назначает порт)
ENV PORT=8080

# Запускаем приложение
CMD ["python", "bot/webhook_server.py"]