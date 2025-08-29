# 🚀 Quick Azure Deployment Guide

## Ready to Deploy Your Procurement Dashboard!

I've prepared everything you need to deploy your dashboard to Azure. Here's what I've created for you:

### 📁 New Files Added:
- `deploy-azure.ps1` - PowerShell deployment script
- `web.config` - Azure configuration
- `Dockerfile` - Container deployment option
- `AZURE_DEPLOYMENT.md` - Detailed deployment guide

## 🎯 Quick Start (Recommended Method)

### Step 1: Install Azure CLI
```powershell
# Download from: https://aka.ms/installazurecliwindows
# Or install via PowerShell:
winget install Microsoft.AzureCLI
```

### Step 2: Run the Deployment Script
```powershell
# Open PowerShell as Administrator in your project folder
cd c:\Users\kiran\procurement-dashboard

# Run the deployment script
.\deploy-azure.ps1
```

### Step 3: Deploy Your Code
```powershell
# After the script completes, add Azure remote (it will show you the command)
git remote add azure [YOUR_DEPLOYMENT_URL]

# Deploy your code
git add .
git commit -m "Deploy to Azure"
git push azure main
```

## 🌐 What You'll Get

Your dashboard will be available at:
`https://procurement-dashboard-[timestamp].azurewebsites.net`

### Features Enabled:
✅ **Auto-scaling** - Handles traffic spikes
✅ **HTTPS** - Secure connections
✅ **Custom domain** - Can add your own domain later
✅ **Monitoring** - Built-in Azure monitoring
✅ **Auto-deployment** - Git push to deploy

## 💰 Cost Estimation

- **B1 Basic Plan**: ~$13-15/month
- **Free Tier**: Available for testing (limited)
- **Scaling**: Can upgrade/downgrade anytime

## 🔧 What I've Already Configured

### Backend Changes:
- ✅ Auto-detects Azure environment
- ✅ Uses Azure's PORT environment variable
- ✅ Production/development mode switching

### Frontend Changes:
- ✅ Auto-detects Azure URLs
- ✅ Fallback to demo mode if backend unavailable
- ✅ Works with custom domains

### Azure Configuration:
- ✅ Python 3.9 runtime
- ✅ Auto-build on deployment
- ✅ Application logging enabled
- ✅ Git deployment configured

## 🚨 Important Notes

1. **App Name**: Must be globally unique (script adds timestamp)
2. **Resource Group**: Will be created automatically
3. **Location**: Set to "East US" (can be changed)
4. **Data**: Your CSV file will be deployed with the app

## 🆘 Need Help?

### Common Issues:
- **Login Required**: Script will prompt you to login to Azure
- **Name Conflicts**: Script uses timestamp to ensure uniqueness
- **Build Errors**: Check Azure logs: `az webapp log tail --name [YOUR_APP_NAME] --resource-group procurement-dashboard-rg`

### Support Resources:
- Azure CLI Documentation: https://docs.microsoft.com/en-us/cli/azure/
- Azure App Service: https://docs.microsoft.com/en-us/azure/app-service/

## 🎉 Ready to Deploy?

1. Open PowerShell as Administrator
2. Navigate to your project: `cd c:\Users\kiran\procurement-dashboard`
3. Run: `.\deploy-azure.ps1`
4. Follow the script output instructions

Your procurement dashboard will be live on Azure in about 5-10 minutes! 🚀
