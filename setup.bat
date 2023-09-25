@echo off

REM Check if Python is installed
python --version
IF %ERRORLEVEL% NEQ 0 (
    
    echo initiating python installation...
    REM Python is not installed, so installing it....
    set PYTHON_VERSION=3.10.5
    set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
    set PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe

    REM Downloading Python installer...
    echo downloading python installer...
    curl -O %PYTHON_INSTALLER% %PYTHON_URL%

    echo installing python silently....
    REM Installing Python silently (assuming default installation path)...
    %PYTHON_INSTALLER% /passive InstallAllUsers=1 PrependPath=1

    echo cleaning up python installer...
    REM Cleaning up the installer...
    del %PYTHON_INSTALLER%

    echo Python %PYTHON_VERSION% has been installed successfully.
) else (
    echo python is already installed. requirement already satisfied.
)

PAUSE
echo postgres check...
@REM postgres --version
@REM IF %ERRORLEVEL% NEQ 0 (
REM Define PostgreSQL version and download URL

set PG_VERSION=15.2
set PG_URL=https://get.enterprisedb.com/postgresql/postgresql-%PG_VERSION%-windows-x64-binaries.zip

REM Define installation and data directories
set PG_INSTALL_DIR=C:\PostgreSQL
set PG_DATA_DIR=C:\PostgreSQL\data

REM Define password for the PostgreSQL 'postgres' user
set PG_PASSWORD=12345
PAUSE

REM create directory
if not exist "pgsql" (
    REM create directory
    mkdir pgsql
) else (
    echo folder already exists...
    
)
PAUSE
cd pgsql
if not exist "postgresql-15.2-2-windows-x64" (
    echo downloading postgres...
    
    curl -O https://ftp.postgresql.org/pub/source/v15.2/postgresql-15.2.tar.bz2
    echo downloaded postgres installer successfully...
) else (
    echo zip file already exists...skipping download
)
@REM curl -O postgresql.zip %PG_URL%
PAUSE
echo installing postgres...
postgresql-15.2-2-windows-x64.exe
@REM powershell -command "Expand-Archive -Path 'postgresql-15.2.tar'"
PAUSE
REM Unzip the PostgreSQL binaries
@REM powershell -Command "Expand-Archive -Path 'postgresql-15.2.tar'"
REM Set up data directory
@REM mkdir "%PG_DATA_DIR%"
echo initializing database cluster...
REM Initialize the database cluster
"%PG_INSTALL_DIR%\pgsql\bin\initdb.exe" -D "%PG_DATA_DIR%"

echo starting postgres server...
REM Start the PostgreSQL server
"%PG_INSTALL_DIR%\pgsql\bin\pg_ctl.exe" -D "%PG_DATA_DIR%" -l logfile start

REM Create a password for the 'postgres' user
echo ALTER USER postgres WITH PASSWORD ^^^^'%PG_PASSWORD%^^^^'; | "%PG_INSTALL_DIR%\pgsql\bin\psql.exe" -U postgres

echo PostgreSQL %PG_VERSION% has been installed successfully.
@REM ) else (
    @REM echo postgres is already installed. requirement already satisfied.
@REM )
PAUSE

echo cloning from https://github.com/Adhithya-Pinghley/DentalCareTestRepo.git ...
echo archiving repository...
REM Define the GitHub repository details
set GITHUB_USER= Adhithya-Pinghley
set GITHUB_REPO= DentalCareTestRepo
set GITHUB_URL=https://github.com/Adhithya-Pinghley/DentalCareTestRepo/archive/refs/heads/Adhithya.zip
if not exist "Dental-Software" (
mkdir Dental-Software
) else (
    echo folder already exists...
)
PAUSE

cd Dental-Software
REM Define the destination folder where the repository will be extracted
@REM set DESTINATION_FOLDER= Dental-Software
echo downloading the repository (including dependencies)...
REM Download the repository as a ZIP archive using curl
if not exist "DentalCareTestRepo-Adhithya.zip" (
curl -LJO %GITHUB_URL%
) else (
    echo repository archive already exists. Skipping download...
)
PAUSE
if not exist "DentalCareTestRepo-Adhithya" (
echo extracting repository with dependencies...
REM Extract the contents of the ZIP archive
powershell -command "Expand-Archive -Path 'DentalCareTestRepo-Adhithya.zip'"
@REM -DestinationPath '%DESTINATION_FOLDER%'
) else (
    echo repository already extracted. Skipping extraction...
)
PAUSE

echo cleaning up archives...
REM Clean up the ZIP archive
@REM del Adhithya.zip
echo The GitHub repository has been downloaded and installed successfully.

PAUSE
cd DentalCareTestRepo-Adhithya\DentalCareTestRepo-Adhithya
REM Create a virtual environment
python -m venv .venv

PAUSE

echo Virtual environment created...

PAUSE
echo activating virtual environment...
REM Set the path to the virtual environment activation script
set VENV_PATH=.venv\Scripts\activate

PAUSE

REM Activate the virtual environment
call %VENV_PATH%

PAUSE
cd NandhaKumaranDentalClinic\NandhaKumaranDental
echo running database migrations...
REM Run database migrations
python manage.py makemigrations
python manage.py migrate
echo migrations created...
PAUSE

echo starting Django development server
REM Start the Django development server
python manage.py runserver

echo you can now open "127.0.0.1:8000" in your browser... 
PAUSE