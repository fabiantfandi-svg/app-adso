FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade "pip>=24.0" "setuptools>=78.1.1" "wheel>=0.43.0"

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade --force-reinstall -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
