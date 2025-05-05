#!/bin/bash

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "🧪 Running tests with Pytest..."
pytest --maxfail=1 --capture=tee-sys --tb=short