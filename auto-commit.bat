set CURRENT_DATE_TIME=%date:~0,4%-%date:~5,2%-%date:~8,2%-%time:~0,2%:%time:~3,2%:%time:~6,2%

:: …Ë÷√ ±º‰
::echo %CURRENT_DATE_TIME%  
git add .
git commit -m "auto commit: %CURRENT_DATE_TIME%"
git push origin master

cmd /k  
