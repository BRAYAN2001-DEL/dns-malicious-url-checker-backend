# Usa la imagen base de Python 3.8
FROM python:3.8-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias necesarias
RUN pip install -r requirements.txt

# Copia todos los archivos del directorio actual al directorio /app del contenedor
COPY . .

# Define el comando por defecto para ejecutar cuando el contenedor se inicie
CMD ["python", "app.py"]