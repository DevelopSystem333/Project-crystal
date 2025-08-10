import winreg
from Logs.log import clog

def disable_xbox_game_bar():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR",
            0, 
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(key, "AppCaptureEnabled", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, "GameDVR_Enabled", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        clog("Xbox Game Bar отключён в реестре.")
    except Exception as e:
        clog(f"Ошибка: {e}")