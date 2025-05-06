#!/bin/bash

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🧪 Running tests with Pytest..."
pytest --alluredir=allure-results