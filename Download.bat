@REM This program downloads Youtube Videos
@echo off

@REM Get Link input
set /p "link=Type the download link : "

@REM Run python program
wsl bash -c "./dist/Downloader %link%"

@REM Script completed successfully
pause
