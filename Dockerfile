FROM python:3.11-slim

WORKDIR /app

# Устанавливаем только минимальные системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Устанавливаем CPU-only версию PyTorch с правильным индексом
RUN pip install --no-cache-dir torch==2.2.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install --no-cache-dir -r requirements.txt

# Очищаем кэш и удаляем компиляторы
RUN apt-get remove -y gcc g++ \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && pip cache purge

COPY poker_mentor/ ./poker_mentor/

ENV PORT=8080
CMD ["python", "poker_mentor/bot/webhook_server.py"]