#!/bin/bash

rm ./dist/*
rm ./setup.py
rm ./Implug/__init__.py
pip3 uninstall Implug -y

python3 buildInit.py

# pip3 install build
python3 -m build -n
pip3 install dist/*.whl
