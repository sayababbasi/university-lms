@echo off
echo ===================================
echo Pushing Backend...
echo ===================================
cd backend

IF NOT EXIST ".git" (
    echo Initializing git in backend...
    git init
    git branch -M main
    git remote add origin https://github.com/sayababbasi/lms-backend.git
)

git add .
git commit -m "Auto commit %date% %time%"
git push -u origin main

cd ..

echo ===================================
echo Pushing Frontend...
echo ===================================
cd frontend

IF NOT EXIST ".git" (
    echo Initializing git in frontend...
    git init
    git branch -M main
    git remote add origin https://github.com/sayababbasi/lms-frontend.git
)

git add .
git commit -m "Auto commit %date% %time%"
git push -u origin main

cd ..

echo ===================================
echo Push complete!
echo ===================================
pause
