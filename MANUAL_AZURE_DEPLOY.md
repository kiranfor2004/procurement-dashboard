# 🚀 Manual Azure Deployment Steps

## Follow these steps to deploy your Procurement Dashboard to Azure:

### Step 1: Azure Login
```powershell
# Open a new PowerShell window and run:
az login

# If you have MFA, use:
az login --use-device-code
# Then follow the browser instructions
```

### Step 2: Create Azure Resources
```powershell
# Set variables (run these one by one)
$ResourceGroup = "procurement-dashboard-rg"
$AppName = "procurement-dashboard-$(Get-Date -Format 'yyyyMMddHHmmss')"
$Location = "East US"
$PlanName = "procurement-dashboard-plan"

# Create resource group
az group create --name $ResourceGroup --location $Location

# Create App Service plan
az appservice plan create --name $PlanName --resource-group $ResourceGroup --sku B1 --is-linux

# Create web app
az webapp create --resource-group $ResourceGroup --plan $PlanName --name $AppName --runtime "PYTHON|3.9" --deployment-local-git

# Configure app settings
az webapp config appsettings set --resource-group $ResourceGroup --name $AppName --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true FLASK_ENV=production

# Enable logging
az webapp log config --resource-group $ResourceGroup --name $AppName --application-logging filesystem --level information
```

### Step 3: Get Deployment URL
```powershell
# Get the Git deployment URL
$DeploymentUrl = az webapp deployment source config-local-git --resource-group $ResourceGroup --name $AppName --query url --output tsv

# Display the information
Write-Host "App Name: $AppName"
Write-Host "URL: https://$AppName.azurewebsites.net"
Write-Host "Deployment URL: $DeploymentUrl"
```

### Step 4: Deploy Your Code
```powershell
# Add Azure as a Git remote
git remote add azure $DeploymentUrl

# Commit your changes
git add .
git commit -m "Deploy to Azure"

# Push to Azure (this will trigger the deployment)
git push azure main
```

### Step 5: Monitor Deployment
```powershell
# Watch the deployment logs
az webapp log tail --resource-group $ResourceGroup --name $AppName
```

## 🎯 Expected Result

After successful deployment:
- Your app will be available at: `https://[your-app-name].azurewebsites.net`
- The dashboard will automatically detect the Azure environment
- All features will work including charts and filtering

## 🆘 Troubleshooting

### Common Issues:
1. **Login fails**: Use `az login --use-device-code` and complete browser authentication
2. **App name taken**: The timestamp makes it unique, but try again if needed
3. **Build errors**: Check logs with `az webapp log tail`
4. **CSV not found**: Make sure `Purchase data.csv` is in your project root

### Check Status:
```powershell
# Check if app is running
az webapp show --resource-group $ResourceGroup --name $AppName --query state

# Restart if needed
az webapp restart --resource-group $ResourceGroup --name $AppName
```

## 💰 Cost Information
- **B1 Plan**: ~$13-15/month
- **Free tier**: Available for testing (limited)
- **Auto-scaling**: Available on higher tiers

## 🎉 Next Steps After Deployment

1. **Test your dashboard**: Visit the Azure URL
2. **Custom domain**: Can be added later in Azure Portal
3. **SSL certificate**: Automatically provided by Azure
4. **Monitor usage**: Use Azure Portal insights

---

**Ready to start?** Open PowerShell and begin with Step 1! 🚀
