#!/bin/bash

# Quick start script for publishing to PyPI

echo "🚀 LangGraph Cross-Chain Publishing Quick Start"
echo "================================================"
echo ""

# Check Python version
echo "📌 Checking Python version..."
python --version

# Install required tools
echo ""
echo "📦 Installing build tools..."
pip install --upgrade pip setuptools wheel twine build

# Clean previous builds
echo ""
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info/

# Run tests
echo ""
echo "🧪 Running tests..."
pytest tests/ -v --tb=short

if [ $? -ne 0 ]; then
    echo "❌ Tests failed! Fix them before publishing."
    exit 1
fi

# Build the package
echo ""
echo "🏗️ Building package..."
python -m build

# Check the package
echo ""
echo "✅ Checking package..."
twine check dist/*

echo ""
echo "📊 Package contents:"
ls -la dist/

echo ""
echo "✨ Build complete! Next steps:"
echo "1. Test on TestPyPI first:"
echo "   twine upload --repository testpypi dist/*"
echo ""
echo "2. Then publish to PyPI:"
echo "   twine upload dist/*"
echo ""
echo "3. Or use the Python script:"
echo "   python scripts/publish.py"
