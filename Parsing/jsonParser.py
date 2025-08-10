import json
import subprocess
import os

from Logs.log import clog

script_path = r"D:\script.ps1"
commands = []

commands.append("Write-Host 'Starting installation...'")

def load_json_data():
    json_path = './json/apps.json'
    if not os.path.exists(json_path):
        clog(f"Файл {json_path} не найден")
    
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def find_package(data, package_id):
    for package in data['Packages']:
        if package['PackageIdentifier'] == package_id:
            return package
    return None

def add_to_script(package_id):
    try:
        data = load_json_data()
        package = find_package(data, package_id)
        if package:
            commands.append(f"winget install --id {package['PackageIdentifier']} -h --accept-package-agreements")
            return True
        return False
    except Exception as e:
        clog(f"Ошибка добавления {package_id}: {str(e)}")
        return False

def addFirefoxToScript():
    return add_to_script('Mozilla.Firefox')

def addVSCodeToScript():
    return add_to_script('Microsoft.VisualStudioCode')

def add7zipToScript():
    return add_to_script('7zip.7zip')

def executeScript():
    try:
        commands.append("Write-Host 'Installation script completed'")
        
        with open(script_path, 'w', encoding='utf-8-sig') as file:
            file.write("\n".join(commands))
        
        subprocess.Popen(["powershell.exe", "-File", script_path])
        clog("Скрипт выполняется...")
    except Exception as e:
        clog(f"Ошибка в воспроизведении скрипта: {str(e)}")