# Usa la imagen base de Python 3.9 (o la versión que estés usando)
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY app.py /app/app.py
COPY dns_inventory.py /app/dns_inventory.py
COPY url_analysis.py /app/url_analysis.py
COPY requirements.txt /app/requirements.txt

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que corre la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["python", "app.py"]
