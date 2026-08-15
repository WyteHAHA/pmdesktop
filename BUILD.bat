if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist pybuild rmdir /s /q pybuild
call npm run build
pyinstaller --workpath pybuild app.spec

