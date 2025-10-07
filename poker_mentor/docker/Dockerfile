FROM python:3.12-slim

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Создание не-root пользователя
RUN useradd --create-home --shell /bin/bash poker
USER poker

# Запуск приложения
CMD ["python", "run_bot.py"]