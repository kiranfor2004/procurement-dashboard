# Procurement Dashboard - GitHub Setup Script
Write-Host "==========================================="
Write-Host "   Procurement Dashboard - GitHub Setup"
Write-Host "==========================================="
Write-Host ""

# Check if Git is installed
try {
    git --version | Out-Null
    Write-Host "✅ Git found! Initializing repository..." -ForegroundColor Green
}
catch {
    Write-Host "❌ ERROR: Git is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Git from https://git-scm.com/" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

try {
    # Initialize Git repository
    Write-Host "📁 Initializing Git repository..." -ForegroundColor Blue
    git init

    # Add all files
    Write-Host "📄 Adding all files to Git..." -ForegroundColor Blue
    git add .

    # Create initial commit
    Write-Host "💾 Creating initial commit..." -ForegroundColor Blue
    git commit -m "Initial commit: Procurement Dashboard with advanced KPIs, drill-down features, and YTD/MTD filters"

    Write-Host ""
    Write-Host "==========================================="
    Write-Host "    Setup Complete! ✅"
    Write-Host "==========================================="
    Write-Host ""
    Write-Host "📋 Next steps:" -ForegroundColor Yellow
    Write-Host "1. Create a new repository on GitHub.com"
    Write-Host "2. Copy the repository URL"
    Write-Host "3. Run the following commands:"
    Write-Host ""
    Write-Host "   git remote add origin YOUR_GITHUB_URL" -ForegroundColor Cyan
    Write-Host "   git push -u origin main" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "📝 Example:" -ForegroundColor Green
    Write-Host "   git remote add origin https://github.com/yourusername/procurement-dashboard.git" -ForegroundColor Gray
    Write-Host "   git push -u origin main" -ForegroundColor Gray
    Write-Host ""
    Write-Host "🚀 Your files are ready for GitHub!" -ForegroundColor Green

}
catch {
    Write-Host "❌ Error during Git setup: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
Read-Host "Press Enter to continue"
