FROM python:3.10-slim

WORKDIR /app

# Crear un entorno virtual aislado y ponerlo en el PATH
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Actualizar las herramientas base dentro del entorno virtual
RUN pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" wheel

# Instalar las dependencias de la aplicación
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
