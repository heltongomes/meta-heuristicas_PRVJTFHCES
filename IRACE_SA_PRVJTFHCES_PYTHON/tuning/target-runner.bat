@echo off
SET "exe=C:\GitHub\otimizacao-combinatoria\IRACE_SA_PRVJTFHCES_PYTHON\programa\main.py"
SET "fixed_params= "

FOR /f "tokens=1-4*" %%a IN ("%*") DO (
	SET candidate=%%a
	SET instance_id=%%b
	SET seed=%%c
	SET instance=%%d
	SET candidate_parameters=%%e
)

SET "stdout=c%candidate%-%instance_id%-%seed%.stdout"
SET "stderr=c%candidate%-%instance_id%-%seed%.stderr"

python %exe% -i %instance% %candidate_parameters% 1>%stdout% 2>%stderr%

set "LINES=0"
for /f "delims==" %%I in (%stdout%) DO set /a LINES = LINES+1

set /a lastline=%LINES%-1
more +%lastline% %stdout%

del %stdout% %stderr%

exit 0