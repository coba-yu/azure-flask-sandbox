# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /code
COPY pyproject.toml ./
COPY requirements.lock ./
RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -r requirements.lock

COPY src ./src

EXPOSE 50505

WORKDIR /code/src
ENTRYPOINT ["gunicorn", "-c", "/code/src/backend/gunicorn.conf.py", "backend.app:app"]
