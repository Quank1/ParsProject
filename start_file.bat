@echo off

python -m venv venv

cd venv/Scripts

start activate.bat

pip install request, beAautifulsoup4, lxml

python main.py

pause