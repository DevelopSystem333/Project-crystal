import winreg

def restore_win10_context_menu():
    try:
        # Открываем ключ реестра
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32",
            0,
            winreg.KEY_WRITE
        )
    except FileNotFoundError:
        # Если ключа нет — создаём
        key = winreg.CreateKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32"
        )
    
    # Устанавливаем пустое значение (это отключает новое меню)
    winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "")
    winreg.CloseKey(key)
    
    print("Контекстное меню Windows 10 восстановлено. Перезапустите проводник или перезагрузите ПК.")