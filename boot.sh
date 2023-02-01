#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "Running Development Server"
    exec python "birds.py" dev
else
    echo "Running Production Server"
    exec python "birds.py" prod
fi
