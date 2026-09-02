FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir --upgrade --force-reinstall -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
