if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
call npm run build
if exist pybuild rmdir /s /q pybuild
pyinstaller --noconsole --onefile --workpath pybuild --add-data "build;build" app.py

