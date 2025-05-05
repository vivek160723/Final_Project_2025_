#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "🧪 Running tests with Pytest..."
pytest --alluredir=allure-results --disable-warnings

echo "📊 Generating Allure report..."
/Users/vivekkumar/.jenkins/tools/ru.yandex.qatools.allure.jenkins.tools.AllureCommandlineInstallation/Allure/bin/allure generate allure-results -c -o allure-report

echo "✅ Allure report generated successfully at: allure-report"