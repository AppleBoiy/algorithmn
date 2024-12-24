#!/bin/bash

python setup.py sdist bdist_wheel

pip install ./dist/thealgorithm-0.1.0-py3-none-any.whl --force-reinstall
