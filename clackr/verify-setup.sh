#!/bin/bash

# Clackr Setup Verification Script
# This script verifies that Clackr is properly set up

echo "🔍 Clackr Setup Verification"
echo "============================="
echo ""

# Check Node.js
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo "✓ Node.js installed: $NODE_VERSION"
else
    echo "✗ Node.js not found"
    exit 1
fi

# Check npm
if command -v npm &> /dev/null; then
    NPM_VERSION=$(npm --version)
    echo "✓ npm installed: $NPM_VERSION"
else
    echo "✗ npm not found"
    exit 1
fi

# Check project files
echo ""
echo "📁 Project Files:"
REQUIRED_FILES=("bin/clackr.js" "bin/server.js" "package.json" "vercel.json")

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "✓ $file"
    else
        echo "✗ $file (missing)"
    fi
done

# Check node_modules
if [ -d "node_modules" ]; then
    echo "✓ Dependencies installed"
else
    echo "✗ Dependencies not installed"
    echo "  Run: npm install"
    exit 1
fi

# Check key dependencies
echo ""
echo "📦 Key Dependencies:"
DEPS=("socket.io" "socket.io-client" "chalk" "inquirer" "express")

for dep in "${DEPS[@]}"; do
    if [ -d "node_modules/$dep" ]; then
        echo "✓ $dep"
    else
        echo "✗ $dep (missing)"
    fi
done

echo ""
echo "✅ Setup verification complete!"
echo ""
echo "Next steps:"
echo "1. Start the server: npm run dev"
echo "2. In another terminal: npm start"
echo ""
echo "For deployment: vercel --prod"
