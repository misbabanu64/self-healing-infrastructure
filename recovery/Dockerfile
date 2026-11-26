FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    ansible \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://get.docker.com -o /tmp/get-docker.sh \
    && sh /tmp/get-docker.sh \
    && rm /tmp/get-docker.sh

WORKDIR /app

RUN pip install --no-cache-dir Flask

COPY webhook.py /app/webhook.py

EXPOSE 5000

CMD ["python", "/app/webhook.py"]
