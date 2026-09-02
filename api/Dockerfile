FROM python:3.10-slim

WORKDIR /app

# 1. Clean out default outdated global packages/dist-info
RUN rm -rf /usr/local/lib/python3.10/site-packages/setuptools* \
           /usr/local/lib/python3.10/site-packages/msgpack*

# 2. Upgrade core tooling to secure versions
RUN pip install --no-cache-dir --upgrade "pip>=24.0" "setuptools>=78.1.1" "wheel>=0.43.0"

# 3. Install application dependencies cleanly
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade --force-reinstall -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
