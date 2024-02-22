@echo off
SETLOCAL EnableExtensions

:: Clean previous builds
echo Cleaning previous builds...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist *.egg-info rmdir /s /q *.egg-info

:: Package the library
echo Packaging the library...
python setup.py sdist bdist_wheel

:: Upload the package to PyPI
echo Uploading the package to PyPI...
twine upload dist/*

echo Package uploaded successfully!

ENDLOCAL
