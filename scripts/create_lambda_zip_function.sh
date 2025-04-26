#!/bin/bash

# Clean up the function directory
rm -rf function.zip
rm -rf package

# Create temporary directory for the package
mkdir -p package

# Copy the source code to the package directory
cp -r src package/
cp lambda_function.py package/
cp .env package/

# Create the zip file
cd package
zip -r ../function.zip .
cd ..

# Clean up
rm -rf package