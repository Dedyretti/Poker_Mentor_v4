FROM python:3.11-slim

WORKDIR /app

# Копируем requirements и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем ВСЕ файлы проекта
COPY . .

# Ищем и запускаем webhook_server.py автоматически
CMD sh -c "find /app -name webhook_server.py -type f | head -1 | xargs python"