#!/bin/bash

# TIDAS SDK Examples Setup Script
# This script sets up the examples to use the published npm package

echo "🚀 Setting up TIDAS SDK Examples..."
echo ""

# Check if we're in the examples directory
if [ ! -f "package.json" ]; then
    echo "❌ Error: Please run this script from the examples directory"
    echo "   cd examples && ./setup.sh"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
npm install

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "🧪 Testing imports..."
npm run test-imports

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Setup complete! All imports working correctly."
    echo ""
    echo "Available commands:"
    echo "  npm run test-imports         # Test package imports"
    echo "  npm run run-basic           # Basic entity usage examples"
    echo "  npm run run-validation      # Validation configuration demo"
    echo "  npm run run-advanced        # Advanced usage patterns"
    echo "  npm run run-validation-modes # Comprehensive validation modes"
    echo ""
    echo "Example usage:"
    echo "  npm run run-basic"
    echo ""
else
    echo ""
    echo "⚠️  Setup completed but import test failed."
    echo "   You may need to check the package version or network connection."
    echo ""
fi