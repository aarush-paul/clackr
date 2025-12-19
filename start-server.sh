#!/bin/bash

# Clackr Development Server Start Script

echo "🚀 Starting Clackr Development Server..."
echo ""
echo "Server URL: http://localhost:3000"
echo "WebSocket Endpoint: ws://localhost:3000"
echo ""
echo "To use the CLI client, open another terminal and run:"
echo "  export CLACKR_SERVER=http://localhost:3000"
echo "  npm start"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

NODE_ENV=development PORT=3000 node bin/server.js
