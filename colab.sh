#!/bin/bash

# This script sets up a Google Colab environment for running a specific project(Zank).

# Run launch.py and capture its output
PROXY_OUTPUT=$(python3 launch.py 2>/dev/null)
url_5173=$(echo "$PROXY_OUTPUT" | jq -r '.["5173"]')

# Update the config.js file with the proxy URL
sed -i '' "s|baseUrl: '[^']*'|baseUrl: '$url_5173'|" frontend/config.js
