FROM python:3.11.6-slim-bullseye AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11.6-slim-bullseye

COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH

WORKDIR /app

COPY . .

CMD ["python", "-m", "main"]