@REM This program downloads Youtube Videos
@echo off

@REM Get Link input
set /p "link=Type the download link : "

@REM Activate the virtual environment
call .venv\Scripts\activate.bat

@REM Run python program
cd src\
python main.py %link%

@REM Script completed successfully
pause
