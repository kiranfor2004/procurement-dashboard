# Azure Deployment Guide for Procurement Dashboard

## Prerequisites
1. Azure Account (Free tier available)
2. Azure CLI installed
3. Git repository (already set up)

## Method 1: Azure App Service (Recommended)

### Step 1: Install Azure CLI
```bash
# Download and install from: https://aka.ms/installazurecliwindows
# Or use PowerShell:
Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi; Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'
```

### Step 2: Login to Azure
```bash
az login
```

### Step 3: Create Resource Group
```bash
az group create --name procurement-dashboard-rg --location "East US"
```

### Step 4: Create App Service Plan
```bash
az appservice plan create --name procurement-dashboard-plan --resource-group procurement-dashboard-rg --sku B1 --is-linux
```

### Step 5: Create Web App
```bash
az webapp create --resource-group procurement-dashboard-rg --plan procurement-dashboard-plan --name your-unique-app-name --runtime "PYTHON|3.9" --deployment-local-git
```

### Step 6: Configure App Settings
```bash
az webapp config appsettings set --resource-group procurement-dashboard-rg --name your-unique-app-name --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true
```

### Step 7: Deploy Code
```bash
# Add Azure remote
git remote add azure https://your-unique-app-name.scm.azurewebsites.net:443/your-unique-app-name.git

# Push to Azure
git push azure main
```

## Method 2: Azure Static Web Apps + Azure Functions

### For Frontend (Static Web App)
1. Go to Azure Portal
2. Create "Static Web App"
3. Connect to your GitHub repository
4. Set build details:
   - App location: "/"
   - Output location: "/"

### For Backend (Azure Functions)
1. We'll convert your Flask app to Azure Functions
2. Create Azure Function App
3. Deploy Python functions

## Method 3: Container Deployment

### Using Azure Container Instances
1. Create Dockerfile
2. Build container image
3. Deploy to Azure Container Registry
4. Run on Azure Container Instances

## Post-Deployment Steps

### 1. Custom Domain (Optional)
```bash
az webapp config hostname add --webapp-name your-unique-app-name --resource-group procurement-dashboard-rg --hostname yourdomain.com
```

### 2. SSL Certificate
```bash
az webapp config ssl bind --certificate-thumbprint {thumbprint} --ssl-type SNI --name your-unique-app-name --resource-group procurement-dashboard-rg
```

### 3. Monitor Performance
- Enable Application Insights
- Set up monitoring and alerts

## Estimated Costs
- **Basic Plan (B1)**: ~$13-15/month
- **Free Tier**: Available for testing
- **Static Web Apps**: Free tier available

## Next Steps After Reading This Guide
1. Choose your deployment method
2. Replace "your-unique-app-name" with your preferred name
3. Run the commands in order
4. Test your deployed application

## Support
- Azure Documentation: https://docs.microsoft.com/en-us/azure/app-service/
- Azure CLI Reference: https://docs.microsoft.com/en-us/cli/azure/
