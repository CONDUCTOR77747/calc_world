#!/bin/bash

# Extract command-line arguments
FILES_TO_CHECK="$@"

# Run pylint
echo "PYLINT"
pylint $FILES_TO_CHECK

# Run mypy
echo "MYPY"
mypy --strict $FILES_TO_CHECK

# Run flake8
echo "FLAKE8"
flake8 $FILES_TO_CHECK

# Run pytest
echo "PYTEST"
pytest