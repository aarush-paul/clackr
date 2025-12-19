#!/bin/bash

# Build script for Clackr

echo "📦 Building Clackr..."

# Install dependencies
echo "Installing dependencies..."
npm ci

# Verify structure
echo "Verifying project structure..."
if [ ! -f "bin/clackr.js" ]; then
  echo "❌ Error: bin/clackr.js not found"
  exit 1
fi

if [ ! -f "bin/server.js" ]; then
  echo "❌ Error: bin/server.js not found"
  exit 1
fi

echo "✓ Build successful!"
echo ""
echo "To start the server:"
echo "  npm run dev"
echo ""
echo "To start the CLI:"
echo "  npm start"
