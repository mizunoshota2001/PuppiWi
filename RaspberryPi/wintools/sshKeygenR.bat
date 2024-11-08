@echo off
setlocal 
cd %~dp0 && call config.bat

ssh-keygen -R %HOST%