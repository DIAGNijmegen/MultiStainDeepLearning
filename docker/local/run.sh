#!/bin/bash

# Determine the directory where this script is located
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# Navigate to the project root directory
cd "$SCRIPT_DIR/../.."

docker run --rm -it --gpus all -p 8888:8888 -v $(pwd):/usr/home/project_sync multistain
