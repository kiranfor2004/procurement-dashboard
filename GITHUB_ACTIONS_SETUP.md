# Azure App Service Deployment Setup Guide

## Prerequisites
1. Azure App Service created
2. GitHub repository with your code
3. Azure publish profile configured

## Setup Steps

### 1. Get Azure App Service Publish Profile
```bash
# Login to Azure CLI
az login

# Get the publish profile for your app service
az webapp deployment list-publishing-profiles --name Procurementdashboard --resource-group pROCUREMENT-DASHBOARD --xml
```

### 2. Configure GitHub Secrets
1. Go to your GitHub repository: https://github.com/kiranfor2004/procurement-dashboard
2. Navigate to Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Add the following secrets:

**Secret Name:** `AZURE_WEBAPP_PUBLISH_PROFILE`
**Secret Value:** [Paste the entire XML content from step 1]

### 3. Update Workflow Configuration
Edit `.github/workflows/azure-webapp-deploy.yml` and update:
```yaml
env:
  AZURE_WEBAPP_NAME: 'Procurementdashboard'  # Your actual app name
```

### 4. Create Azure App Service (if not already created)
```bash
# Create resource group (if not exists)
az group create --name pROCUREMENT-DASHBOARD --location "West Central US"

# Create App Service plan
az appservice plan create --name procurement-dashboard-plan --resource-group pROCUREMENT-DASHBOARD --sku B1 --is-linux

# Create web app
az webapp create --resource-group pROCUREMENT-DASHBOARD --plan procurement-dashboard-plan --name Procurementdashboard --runtime "PYTHON|3.11" --deployment-local-git

# Configure startup command
az webapp config set --resource-group pROCUREMENT-DASHBOARD --name Procurementdashboard --startup-file "gunicorn --bind=0.0.0.0 --timeout 600 app:app"
```

### 5. Manual Deployment Commands (Alternative)
If you prefer manual deployment:

```bash
# Set deployment credentials
az webapp deployment user set --user-name your-deployment-username --password your-deployment-password

# Get Git deployment URL
az webapp deployment source show --name Procurementdashboard --resource-group pROCUREMENT-DASHBOARD

# Add Azure remote and deploy
git remote add azure https://your-deployment-username@Procurementdashboard.scm.azurewebsites.net/Procurementdashboard.git
git push azure main
```

## Workflow Features
- **Automatic Deployment:** Triggers on every push to main branch
- **Manual Trigger:** Can be triggered manually from GitHub Actions tab
- **Python Environment:** Sets up Python 3.11 with virtual environment
- **Dependency Installation:** Automatically installs requirements.txt
- **Artifact Creation:** Creates deployment package excluding unnecessary files
- **Production Environment:** Deploys to production environment with URL output

## Testing the Deployment
1. Push changes to main branch
2. Check GitHub Actions tab for workflow status
3. Access your app at: https://procurementdashboard-h4akgqg7hvbudzhb.westcentralus-01.azurewebsites.net

## Troubleshooting
- Check GitHub Actions logs for deployment issues
- Verify Azure publish profile is correctly set in secrets
- Ensure app name matches in workflow file
- Check Azure App Service logs for runtime issues

## File Structure
```
.github/
  workflows/
    azure-webapp-deploy.yml  # GitHub Actions workflow
requirements.txt             # Python dependencies (includes gunicorn)
startup.txt                 # Azure App Service startup command
web.config                  # Azure App Service configuration
app.py                      # Main Flask application
```
