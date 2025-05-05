#!/bin/bash
set -e

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "🧪 Running tests with Pytest..."
# Suppress LibreSSL warnings during Jenkins execution
PYTHONWARNINGS="ignore::urllib3.exceptions.NotOpenSSLWarning" pytest --alluredir=allure-results

echo "📊 Generating Allure report..."
allure generate allure-results -c -o allure-report
echo "✅ Allure report generated successfully at: allure-report"