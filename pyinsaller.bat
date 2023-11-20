@echo off
cls

:del
if exist .\*.exe (
	del *.exe
)

:exe
pyinstaller --icon=./icon.ico --onefile -w -n=SoundControlProgram main.py

:copy
copy .\dist\SoundControlProgram.exe .\
del .\SoundControlProgram.spec
rmdir /s /q build dist

pause
@echo on