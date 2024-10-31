@echo off
setlocal 
call config.bat

:loop
if "%SSH_KEY_PATH%"=="" (
    ssh %USER%@%HOST%
) else (
    ssh -i "%SSH_KEY_PATH%" %USER%@%HOST%
)
goto loop
