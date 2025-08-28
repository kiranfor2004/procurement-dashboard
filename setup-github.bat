@echo off
echo ===========================================
echo    Procurement Dashboard - GitHub Setup
echo ===========================================
echo.

REM Check if Git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git from https://git-scm.com/
    pause
    exit /b 1
)

echo Git found! Initializing repository...
echo.

REM Initialize Git repository
echo Initializing Git repository...
git init

REM Add all files
echo Adding all files to Git...
git add .

REM Create initial commit
echo Creating initial commit...
git commit -m "Initial commit: Procurement Dashboard with advanced KPIs, drill-down features, and YTD/MTD filters"

echo.
echo ===========================================
echo    Setup Complete!
echo ===========================================
echo.
echo Next steps:
echo 1. Create a new repository on GitHub.com
echo 2. Copy the repository URL
echo 3. Run: git remote add origin YOUR_GITHUB_URL
echo 4. Run: git push -u origin main
echo.
echo Example:
echo git remote add origin https://github.com/yourusername/procurement-dashboard.git
echo git push -u origin main
echo.
echo Your files are ready for GitHub!
echo.
pause
