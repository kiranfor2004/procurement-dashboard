#!/bin/bash

# Azure Deployment Script for Procurement Dashboard
# Run this script to deploy your dashboard to Azure

# Configuration
RESOURCE_GROUP="procurement-dashboard-rg"
APP_NAME="procurement-dashboard-$(date +%s)"  # Adds timestamp for uniqueness
LOCATION="East US"
PLAN_NAME="procurement-dashboard-plan"

echo "🚀 Starting Azure deployment for Procurement Dashboard..."
echo "📋 App Name: $APP_NAME"
echo "📍 Location: $LOCATION"

# Check if Azure CLI is installed
if ! command -v az &> /dev/null; then
    echo "❌ Azure CLI is not installed. Please install it first:"
    echo "   https://docs.microsoft.com/en-us/cli/azure/install-azure-cli"
    exit 1
fi

# Login to Azure (if not already logged in)
echo "🔐 Checking Azure login status..."
if ! az account show &> /dev/null; then
    echo "🔑 Please login to Azure..."
    az login
fi

# Create resource group
echo "📦 Creating resource group: $RESOURCE_GROUP"
az group create --name $RESOURCE_GROUP --location "$LOCATION"

# Create App Service plan
echo "⚡ Creating App Service plan: $PLAN_NAME"
az appservice plan create \
    --name $PLAN_NAME \
    --resource-group $RESOURCE_GROUP \
    --sku B1 \
    --is-linux

# Create web app
echo "🌐 Creating web app: $APP_NAME"
az webapp create \
    --resource-group $RESOURCE_GROUP \
    --plan $PLAN_NAME \
    --name $APP_NAME \
    --runtime "PYTHON|3.9" \
    --deployment-local-git

# Configure app settings
echo "⚙️ Configuring app settings..."
az webapp config appsettings set \
    --resource-group $RESOURCE_GROUP \
    --name $APP_NAME \
    --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true FLASK_ENV=production

# Enable logging
echo "📝 Enabling application logging..."
az webapp log config \
    --resource-group $RESOURCE_GROUP \
    --name $APP_NAME \
    --application-logging filesystem \
    --level information

# Get deployment credentials
echo "🔑 Getting deployment credentials..."
DEPLOYMENT_URL=$(az webapp deployment source config-local-git \
    --resource-group $RESOURCE_GROUP \
    --name $APP_NAME \
    --query url \
    --output tsv)

echo ""
echo "✅ Azure resources created successfully!"
echo ""
echo "📋 Deployment Information:"
echo "   Resource Group: $RESOURCE_GROUP"
echo "   App Name: $APP_NAME"
echo "   URL: https://$APP_NAME.azurewebsites.net"
echo "   Deployment URL: $DEPLOYMENT_URL"
echo ""
echo "🚀 Next Steps:"
echo "1. Add Azure remote: git remote add azure $DEPLOYMENT_URL"
echo "2. Deploy code: git push azure main"
echo "3. Monitor logs: az webapp log tail --resource-group $RESOURCE_GROUP --name $APP_NAME"
echo ""
echo "💡 Pro tip: Save your app name for future reference: $APP_NAME"
