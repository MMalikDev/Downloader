@REM This program downloads Youtube Videos
@echo off

@REM Get Link input
set /p "link=Type the download link : "

@REM Run executable file
cd dist

Downloader.exe %link%

@REM Script completed successfully
pause
