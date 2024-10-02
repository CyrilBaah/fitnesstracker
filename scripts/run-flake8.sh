#!/bin/bash

# Go to root folder
cd $(dirname $0)/..

# Check for issues
echo "Checking for issues with Flake8..."
flake8 .

# If there are issues, exit with non-zero status
if [ $? -ne 0 ]; then
  echo "Flake8 found issues, please fix them. | https://flake8.pycqa.org/en/latest/user/error-codes.html"
  exit 1
fi

echo "No issues with Flake8."
