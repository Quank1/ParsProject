@echo off

python -m venv venv

call venv/Scripts/activate

pip install requests
pip install beautifulsoup4
pip install lxml

python main.py

pause
