#!/bin/bash

# Crear directorio temporal para el paquete
mkdir -p package

# Instalar dependencias en el directorio del paquete
pip install -r requirements.txt --target ./package

# Copiar el código fuente al directorio del paquete
cp -r src package/
cp lambda_function.py package/

# Crear el archivo .env con las variables de entorno necesarias
cp .env package/

# Asegurarse de que el archivo de credenciales esté en el lugar correcto
mkdir -p package/src/config
cp src/config/virtus-automate-4d905345bfa9.json package/src/config/

# Crear el archivo zip
cd package
zip -r ../lambda_deployment.zip .
cd ..

echo "Package lambda_deployment.zip created successfully" 