# Dockerfile for auth_service
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

COPY wait-for-it.sh /wait-for-it.sh

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/wait-for-it.sh", "kafka:9092", "--timeout=30", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
