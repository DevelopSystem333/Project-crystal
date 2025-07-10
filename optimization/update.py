import winreg

def disable_windows_updates():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU",
            0,
            winreg.KEY_WRITE
        )
    except FileNotFoundError:
        key = winreg.CreateKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"
        )
    
    winreg.SetValueEx(key, "NoAutoUpdate", 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(key, "AUOptions", 0, winreg.REG_DWORD, 2)  # 2 - Notify before download
    winreg.CloseKey(key)
    print("Автоматические обновления Windows отключены.")