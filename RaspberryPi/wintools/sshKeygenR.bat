@echo off
setlocal 
call config.bat

ssh-keygen -R %HOST%