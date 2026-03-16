FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.11-alpine

WORKDIR /app

RUN adduser -D appuser

COPY --from=builder /app /app

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]