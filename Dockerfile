FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]

