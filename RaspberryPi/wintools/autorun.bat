@echo off
ssh-keygen -R puppet.local
ssh -o StrictHostKeyChecking=no puppet@puppet.local "cd remote-puppet && python main.py"
pause
