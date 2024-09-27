@echo off
REM Create a virtual environment
python -m venv venv
call venv\Scripts\activate

REM Install required packages
pip install -r requirements.txt

REM Set path for Allure
setx PATH "%PATH%;C:\Users\Dell\Desktop\Swag_Labs_automation\sauce_automation\allure-2.13.5\bin"

REM Run Behave with Allure formatter
behave -f allure_behave.formatter:AllureFormatter -o AllureReports

REM Serve Allure report
allure serve AllureReports
