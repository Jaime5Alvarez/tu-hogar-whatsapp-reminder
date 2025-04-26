#!/bin/bash

# Clean up the layer directory
rm -rf layer.zip

# Create temporary directory for the layer
mkdir -p layer/python

# Install dependencies in the layer directory
uv pip install -r requirements.txt --target ./layer/python

# Create the zip file
cd layer
zip -r ../layer.zip .
cd ..

# Cleanup
rm -rf layer

echo "Layer creado correctamente como layer.zip"
