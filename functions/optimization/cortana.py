import winreg
from Logs.log import clog

def disable_cortana():
    try:
        # Открываем ключ реестра
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Policies\Microsoft\Windows\Windows Search",
            0,
            winreg.KEY_SET_VALUE | winreg.KEY_WOW64_64KEY
        )
        # Устанавливаем значение для отключения Cortana
        winreg.SetValueEx(key, "AllowCortana", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        clog("Cortana отключена через реестр.")
    except FileNotFoundError:
        # Если ключа нет, создаём его
        try:
            key = winreg.CreateKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"SOFTWARE\Policies\Microsoft\Windows\Windows Search"
            )
            winreg.SetValueEx(key, "AllowCortana", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            clog("Cortana отключена (ключ реестра создан).")
        except Exception as e:
            clog(f"Ошибка при создании ключа: {e}")
    except Exception as e:
        clog(f"Ошибка: {e}")