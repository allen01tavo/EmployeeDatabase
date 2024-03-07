@echo OFF 
TITLE Onboarding Installation
echo installing Python libraries needed for execution of onboarding program
echo Process will take a few minutes
echo --------------------------------------------------------------------------------------------------------

echo installing Pywin32
py -m pip install pywin32

echo installing Pywin32
py -m pip install pywin32

echo installing tkclendar
py -m pip install tkcalendar

echo installing 
py -m pip install xlrd

echo installing xlutils
py -m pip install xlutils

echo installing xlwt
py -m pip install xlwt

echo installing tktimepicker
py -m pip install tktimepicker

echo install customtkinter
py -m pip install customtkinter





echo py mainwindow.py >> runApp.bat

.\runApp.bat

