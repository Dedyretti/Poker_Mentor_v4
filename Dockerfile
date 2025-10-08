FROM python:3.11-slim

WORKDIR /app

# Копируем requirements из поддиректории
COPY poker_mentor/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта
COPY poker_mentor/ .

CMD ["python", "bot/webhook_server.py"]