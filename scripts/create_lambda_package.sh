#!/bin/bash

# Create temporary directory for the package
mkdir -p package

# Install dependencies in the package directory
uv pip install -r requirements.txt --target ./package

# Copy the source code to the package directory
cp -r src package/
cp lambda_function.py package/

# Create the .env file with the necessary environment variables
cp .env package/

# Ensure the credentials file is in the correct place
mkdir -p package/src/config
cp src/config/virtus-automate-4d905345bfa9.json package/src/config/

# Create the zip file
cd package
zip -r ../lambda_deployment.zip .
cd ..

# Clean up
rm -rf package

echo "Package lambda_deployment.zip created successfully" 