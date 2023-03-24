#!/bin/sh

set -e

cd $(dirname $0)/..
cd scripts/

# echo "Black Formatting checks"
./run-black.sh

# echo "Isort import sorting checks"
./run-isort.sh 

# echo "Flake8 linting checks"
./run-flake8.sh