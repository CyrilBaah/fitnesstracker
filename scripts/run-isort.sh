#!/bin/bash

# Go to root folder
cd $(dirname $0)/..

# Check for issues
echo "Checking for issues with Python isort..."
isort --check .

# If there are issues, fix them
if [ $? -ne 0 ]; then
  echo "Fixing issues with Python isort..."
  isort .
fi

echo "No issues with Python isort."
