FROM python:3.10-slim

WORKDIR /app

# 1. Crear el entorno virtual aislado
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 2. Actualizar las herramientas dentro del venv
RUN pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" "wheel>=0.46.2"

# 3. Instalar las dependencias de la app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. ELIMINAR los paquetes preinstalados obsoletos del sistema global que Trivy escanea
RUN rm -rf /usr/local/lib/python3.10/site-packages/*

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
