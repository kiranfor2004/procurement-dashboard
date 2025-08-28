# 🚀 GitHub Deployment Guide

## Overview
This guide explains how to deploy the Procurement Dashboard to GitHub and access it from GitHub Pages.

## 📋 Prerequisites
- GitHub account
- Git installed on your local machine
- Your procurement dashboard files ready

## 🔧 Step-by-Step Deployment

### 1. Create GitHub Repository

1. **Go to GitHub.com** and sign in to your account
2. **Click the "+" icon** in the top right corner
3. **Select "New repository"**
4. **Repository Details:**
   - **Name**: `procurement-dashboard` (or your preferred name)
   - **Description**: "Interactive Procurement Analytics Dashboard with Advanced KPIs and Drill-down Reporting"
   - **Visibility**: Choose Public or Private
   - **Initialize**: Don't initialize with README (we have our own)
5. **Click "Create repository"**

### 2. Initialize Local Git Repository

Open PowerShell in your project directory and run:

```powershell
# Navigate to your project directory
cd "C:\Users\kiran\procurement-dashboard"

# Initialize Git repository
git init

# Add all files to staging
git add .

# Create initial commit
git commit -m "Initial commit: Procurement Dashboard with KPIs and drill-down features"

# Add your GitHub repository as origin
git remote add origin https://github.com/YOURUSERNAME/procurement-dashboard.git

# Push to GitHub
git push -u origin main
```

### 3. Enable GitHub Pages

1. **Go to your repository** on GitHub
2. **Click "Settings"** tab
3. **Scroll to "Pages"** in the left sidebar
4. **Source**: Select "Deploy from a branch"
5. **Branch**: Select "main" and "/ (root)"
6. **Click "Save"**

### 4. Access Your Dashboard

After GitHub Pages is enabled (may take a few minutes):

- **Dashboard URL**: `https://YOURUSERNAME.github.io/procurement-dashboard/dashboard.html`
- **Repository URL**: `https://github.com/YOURUSERNAME/procurement-dashboard`

## 🌐 GitHub Pages Configuration

### For Frontend-Only Access

Since GitHub Pages only serves static files, you have two options:

#### Option 1: Static Mode (Recommended for Demo)
The dashboard will work with simulated data when the Flask API is not available.

#### Option 2: External API Hosting
Deploy the Flask backend (`app.py`) to:
- **Heroku**: Free tier available
- **Vercel**: Serverless Python functions
- **Railway**: Simple deployment
- **PythonAnywhere**: Python hosting

### Update API URL for Production

If hosting the API separately, update the API URL in `dashboard.html`:

```javascript
// Change this line in dashboard.html
const API_URL = 'https://your-api-domain.herokuapp.com';
```

## 📁 File Structure on GitHub

```
procurement-dashboard/
├── README.md                   # Project documentation
├── LICENSE                     # MIT License
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
├── app.py                      # Flask backend (needs separate hosting)
├── dashboard.html              # Main dashboard (GitHub Pages compatible)
├── Purchase data.csv           # Data file (145MB)
├── DRILL_DOWN_FEATURES.md      # Feature documentation
├── ENHANCED_KPIS.md            # KPI documentation
└── YTD_MTD_ENHANCEMENT.md      # Enhancement documentation
```

## 🔧 Development Workflow

### Making Updates

```powershell
# Make your changes to files
# Then commit and push:

git add .
git commit -m "Description of your changes"
git push origin main
```

### Branching Strategy

```powershell
# Create feature branch
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Add new feature"

# Push feature branch
git push origin feature/new-feature

# Create Pull Request on GitHub
# Merge to main when ready
```

## 🚀 Production Deployment Options

### Option 1: GitHub Pages + Heroku

1. **Frontend**: GitHub Pages (Free)
   - Serves `dashboard.html` and static files
   - URL: `https://username.github.io/procurement-dashboard/dashboard.html`

2. **Backend**: Heroku (Free tier available)
   - Hosts Flask API (`app.py`)
   - URL: `https://your-app.herokuapp.com`

### Option 2: Full Heroku Deployment

1. **Create Heroku app**
2. **Add Procfile**: `web: python app.py`
3. **Deploy entire project**
4. **Access both frontend and API from Heroku**

### Option 3: Vercel Deployment

1. **Connect GitHub repository to Vercel**
2. **Configure Python runtime**
3. **Deploy with serverless functions**

## 📊 Data Considerations

### Large CSV File (145MB)

The `Purchase data.csv` file is 145MB. Consider:

1. **Git LFS** (Large File Storage) for version control
2. **Separate data hosting** (cloud storage)
3. **Database migration** for production use

### Adding Git LFS (if needed)

```powershell
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.csv"
git add .gitattributes
git commit -m "Add Git LFS for CSV files"
```

## 🔍 Accessing Files from GitHub

### Direct File Access

- **Raw files**: `https://raw.githubusercontent.com/YOURUSERNAME/procurement-dashboard/main/dashboard.html`
- **Repository files**: Browse through GitHub web interface
- **Clone locally**: `git clone https://github.com/YOURUSERNAME/procurement-dashboard.git`

### API Endpoints (when hosted)

- **Summary**: `https://your-api-domain.com/api/summary`
- **Charts**: `https://your-api-domain.com/charts/spend_trend`
- **Filters**: `https://your-api-domain.com/departments`

## 🛠️ Troubleshooting

### Common Issues

1. **GitHub Pages not loading**
   - Check if Pages is enabled in Settings
   - Verify file paths are correct
   - Wait up to 10 minutes for deployment

2. **API not working**
   - Flask backend needs separate hosting
   - Update API_URL in dashboard.html
   - Check CORS settings

3. **Large file issues**
   - Use Git LFS for files > 100MB
   - Consider alternative data hosting

### Local Development

```powershell
# Clone your repository
git clone https://github.com/YOURUSERNAME/procurement-dashboard.git
cd procurement-dashboard

# Create virtual environment
python -m venv dashboard_env
dashboard_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

## 📈 Next Steps

1. **Deploy to GitHub** following the steps above
2. **Enable GitHub Pages** for frontend access
3. **Consider API hosting** for full functionality
4. **Set up CI/CD** for automated deployments
5. **Add collaboration** by inviting team members

## 🎯 Benefits of GitHub Deployment

- **Version Control**: Track all changes and updates
- **Collaboration**: Multiple developers can contribute
- **Documentation**: Comprehensive project documentation
- **Free Hosting**: GitHub Pages provides free static hosting
- **Professional Portfolio**: Showcase your work publicly
- **Backup**: Secure cloud storage of your project

Your procurement dashboard will be accessible worldwide through GitHub Pages, making it easy to share and demonstrate your advanced analytics capabilities!
