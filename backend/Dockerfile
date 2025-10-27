# --- Backend Dockerfile ---
FROM python:3.11-slim

WORKDIR /app

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y build-essential

# Copia los requirements primero (mejor caché)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del backend
COPY app ./app

# Variables de entorno
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

EXPOSE 8000

# Comando de ejecución
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
