# Azure Deployment Script for Procurement Dashboard (PowerShell)
# Run this script to deploy your dashboard to Azure

# Configuration
$ResourceGroup = "procurement-dashboard-rg"
$AppName = "procurement-dashboard-$(Get-Date -Format 'yyyyMMddHHmmss')"  # Adds timestamp for uniqueness
$Location = "East US"
$PlanName = "procurement-dashboard-plan"

Write-Host "🚀 Starting Azure deployment for Procurement Dashboard..." -ForegroundColor Green
Write-Host "📋 App Name: $AppName" -ForegroundColor Yellow
Write-Host "📍 Location: $Location" -ForegroundColor Yellow

# Check if Azure CLI is installed
try {
    $null = az --version
} catch {
    Write-Host "❌ Azure CLI is not installed. Please install it first:" -ForegroundColor Red
    Write-Host "   https://docs.microsoft.com/en-us/cli/azure/install-azure-cli" -ForegroundColor Red
    exit 1
}

# Login to Azure (if not already logged in)
Write-Host "🔐 Checking Azure login status..." -ForegroundColor Cyan
try {
    $null = az account show
} catch {
    Write-Host "🔑 Please login to Azure..." -ForegroundColor Yellow
    az login
}

# Create resource group
Write-Host "📦 Creating resource group: $ResourceGroup" -ForegroundColor Cyan
az group create --name $ResourceGroup --location $Location

# Create App Service plan
Write-Host "⚡ Creating App Service plan: $PlanName" -ForegroundColor Cyan
az appservice plan create `
    --name $PlanName `
    --resource-group $ResourceGroup `
    --sku B1 `
    --is-linux

# Create web app
Write-Host "🌐 Creating web app: $AppName" -ForegroundColor Cyan
az webapp create `
    --resource-group $ResourceGroup `
    --plan $PlanName `
    --name $AppName `
    --runtime "PYTHON|3.9" `
    --deployment-local-git

# Configure app settings
Write-Host "⚙️ Configuring app settings..." -ForegroundColor Cyan
az webapp config appsettings set `
    --resource-group $ResourceGroup `
    --name $AppName `
    --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true FLASK_ENV=production

# Enable logging
Write-Host "📝 Enabling application logging..." -ForegroundColor Cyan
az webapp log config `
    --resource-group $ResourceGroup `
    --name $AppName `
    --application-logging filesystem `
    --level information

# Get deployment credentials
Write-Host "🔑 Getting deployment credentials..." -ForegroundColor Cyan
$DeploymentUrl = az webapp deployment source config-local-git `
    --resource-group $ResourceGroup `
    --name $AppName `
    --query url `
    --output tsv

Write-Host ""
Write-Host "✅ Azure resources created successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Deployment Information:" -ForegroundColor Yellow
Write-Host "   Resource Group: $ResourceGroup" -ForegroundColor White
Write-Host "   App Name: $AppName" -ForegroundColor White
Write-Host "   URL: https://$AppName.azurewebsites.net" -ForegroundColor White
Write-Host "   Deployment URL: $DeploymentUrl" -ForegroundColor White
Write-Host ""
Write-Host "🚀 Next Steps:" -ForegroundColor Yellow
Write-Host "1. Add Azure remote: git remote add azure $DeploymentUrl" -ForegroundColor White
Write-Host "2. Deploy code: git push azure main" -ForegroundColor White
Write-Host "3. Monitor logs: az webapp log tail --resource-group $ResourceGroup --name $AppName" -ForegroundColor White
Write-Host ""
Write-Host "💡 Pro tip: Save your app name for future reference: $AppName" -ForegroundColor Cyan

# Save app info to file for reference
$AppInfo = @"
# Procurement Dashboard - Azure Deployment Info
Resource Group: $ResourceGroup
App Name: $AppName
URL: https://$AppName.azurewebsites.net
Deployment URL: $DeploymentUrl
Deployed: $(Get-Date)

# Useful Commands:
# Monitor logs: az webapp log tail --resource-group $ResourceGroup --name $AppName
# Restart app: az webapp restart --resource-group $ResourceGroup --name $AppName
# Get app info: az webapp show --resource-group $ResourceGroup --name $AppName
"@

$AppInfo | Out-File -FilePath "azure-deployment-info.txt" -Encoding UTF8
Write-Host "📄 Deployment info saved to: azure-deployment-info.txt" -ForegroundColor Green
