@echo off
setlocal 
call config.bat

if "%SSH_KEY_PATH%"=="" (
    ssh %USER%@%HOST%
) else (
    ssh -i "%SSH_KEY_PATH%" %USER%@%HOST%
)