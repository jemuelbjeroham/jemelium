@echo off

:: Change directory to the location of the virtual environment
cd /d "C:\path\to\your\virtualenv"

:: Activate the virtual environment
call Scripts\activate

:: Change directory to the location of your Python script
cd /d "C:\path\to\your\script"

:: Run the Python script
python your_script.py

:: Deactivate the virtual environment
deactivate

pause
