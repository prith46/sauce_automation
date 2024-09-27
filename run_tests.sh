set -e

pip install -r requirements.txt

setx PATH "%PATH%;C:\Users\Dell\Desktop\Swag_Labs_automation\sauce_automation\allure-2.13.5\bin"

behave -f allure_behave.formatter:AllureFormatter -o AllureReports

allure serve AllureReports
