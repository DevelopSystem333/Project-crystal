import winreg

def disable_edge():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Policies\Microsoft\Edge",
            0,
            winreg.KEY_SET_VALUE | winreg.KEY_WOW64_64KEY
        )
        winreg.SetValueEx(key, "EdgeEnabled", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print("Microsoft Edge отключён в реестре.")
    except FileNotFoundError:
        # Если ключа нет, создаём его
        try:
            key = winreg.CreateKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"SOFTWARE\Policies\Microsoft\Edge"
            )
            winreg.SetValueEx(key, "EdgeEnabled", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print("Microsoft Edge заблокирован (ключ реестра создан).")
        except Exception as e:
            print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")