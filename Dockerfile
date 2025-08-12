# builder stage
FROM python:3.13-slim AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --prefix=/install -r requirements.txt

# final stage
FROM python:3.13-slim

WORKDIR /app

ENV PATH="/install/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /install /usr/local
COPY . /app

# Use environment variable for settings module; fallback to dev if not provided
ENV DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE:-Django_TechYatra.settings.dev}

EXPOSE 8000

CMD ["gunicorn", "Django_TechYatra.wsgi:application", "--bind", "0.0.0.0:8000"]