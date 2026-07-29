@echo off
echo Starting Hermes Gateway...
cd /d C:\Users\hongk\.hermes\hermes-agent
C:\Users\hongk\AppData\Local\Programs\Python\Python311\python.exe hermes_cli\main.py gateway run --replace
pause
