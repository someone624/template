#!/bin/bash

# Stop script on any error
set -e

# Arguments: environment (staging/production)
ENV=$1

if [ -z "$ENV" ]; then
  echo "Error: No environment specified. Use 'staging' or 'production'."
  exit 1
fi

# Deployment Configuration
if [ "$ENV" == "staging" ]; then
  TARGET_SERVER="user@staging-server.com"
  TARGET_DIR="/var/www/your-app-staging"
elif [ "$ENV" == "production" ]; then
  TARGET_SERVER="user@production-server.com"
  TARGET_DIR="/var/www/your-app"
else
  echo "Error: Unknown environment '$ENV'. Use 'staging' or 'production'."
  exit 1
fi

BUILD_DIR="dist"

# Build Application
echo "Building application for $ENV..."
npm install
npm run build

# Deploy Build Files to Server
echo "Deploying application to $ENV..."
scp -r $BUILD_DIR/* $TARGET_SERVER:$TARGET_DIR

echo "Deployment to $ENV successful!"
