#!/bin/bash

# This script sets up a Google Colab environment for running a specific project(Zank).

# Run launch.py and capture its output
PROXY_OUTPUT=$(python3 launch.py 2>/dev/null)
url_5173=$(echo "$PROXY_OUTPUT" | jq -r '.["5173"]')
url_8000=$(echo "$PROXY_OUTPUT" | jq -r '.["8000"]')

# Update the config.js file with the proxy URL
sed -i '' "s|baseUrl: '[^']*'|baseUrl: '$url_5173'|g" frontend/config.js

# Update the vite.config.js file with the proxy URL
sed -i '' "s|target: '[^']*'|target: '$url_8000'|g" frontend/vite.config.js
