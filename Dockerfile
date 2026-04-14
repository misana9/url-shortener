FROM python:3.12-slim

WORKDIR /usr/src/app

copy requirements.txt .

run pip install -r requirements.txt

copy . .

CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
