import winreg
from Logs.log import clog

def performance_mode():
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Control Panel\Desktop",
            0,
            winreg.KEY_WRITE
        )

        # Отключаем анимацию окон, но оставляем сглаживание шрифтов
        winreg.SetValueEx(key, "DragFullWindows", 0, winreg.REG_SZ, "0")
        winreg.SetValueEx(key, "FontSmoothing", 0, winreg.REG_SZ, "1")  # 1 - включить сглаживание
        winreg.SetValueEx(key, "UserPreferencesMask", 0, winreg.REG_BINARY, b'\x90\x12\x01\x80\x10\x00\x00\x00')
        winreg.CloseKey(key)

        clog("Настройки применены. Возможно, потребуется перезагрузка.")
    except Exception as e:
        clog(f'Ошибка: {e}')