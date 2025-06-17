@echo off
:: setup_thesis_env.bat
:: Recreates virtual environment for thesis using Python 3.10.11

echo ================================
echo Checking for existing virtual environment...
echo ================================

if exist venv (
    echo Existing venv folder found. Deleting...
    rmdir /s /q venv
) else (
    echo No existing venv found. Proceeding...
)

echo ================================
echo Creating virtual environment...
echo ================================
"D:\Installed\Python 3.10.11\python.exe" -m venv venv

echo ================================
echo Activating virtual environment...
echo ================================
call venv\Scripts\activate.bat

echo ================================
echo Upgrading pip...
echo ================================
python -m pip install --upgrade pip

echo ================================
echo Installing core packages...
echo ================================
pip install torch transformers datasets matplotlib scikit-learn jupyterlab

echo ================================
echo Freezing environment to requirements.txt...
echo ================================
pip freeze > requirements.txt

echo ================================
echo Setup complete!
echo ================================
pause
