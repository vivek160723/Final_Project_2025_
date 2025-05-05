#!/bin/bash
set -e

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "🧪 Running tests with Pytest..."
PYTHONWARNINGS="ignore" pytest --alluredir=allure-results

echo "✅ Pytest completed. Allure report will be handled by Jenkins."