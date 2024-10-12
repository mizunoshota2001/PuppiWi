@echo off
ssh-keygen -R puppet.local
:loop
ssh -o StrictHostKeyChecking=no puppet@puppet.local
if errorlevel 1 goto loop
pause
