from desing import Ui_MainWindow
from Logs.log import clog

def _apply_style_to_elements(window, elements, style):
    """Применяет стиль к списку элементов"""
    if not window or not hasattr(window, 'ui') or not window.ui:
        return False
        
    for element in elements:
        element.setStyleSheet(style)
    return True

def _get_common_elements(ui):
    """Возвращает список общих элементов"""
    return [
        ui.pushButton,
        ui.pushButton_3,
        ui.pushButton_4,
        ui.pushButton_8,
        ui.widget,
        ui.widget_2,
        ui.widget_3,
        ui.widget_4,
        ui.widget_5,
        ui.widget_8,
        ui.widget_9,
        ui.widget_10
    ]

def _get_accent_elements(ui):
    """Возвращает список акцентных элементов"""
    return [
        ui.add7zip,
        ui.addFirefox,
        ui.addVSCode,
        ui.darkTheme,
        ui.lightTheme
    ]

def switchThemeToLight(window):
    if not window or not hasattr(window, 'ui') or not window.ui:
        clog("Предупреждение: не удалось применить светлую тему")
        return

    common_style = 'background-color: rgba(255, 255, 255, 0.3); color: white; border-radius: 5px;'
    accent_style = 'background-color: rgba(255, 255, 255, 0.4); color: white; border-radius: 5px;'
    bg_style = 'background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #b200ff, stop: 0.5 #0500ff, stop: 1 #ff0000);'

    # Применяем стили
    _apply_style_to_elements(window, _get_common_elements(window.ui), common_style)
    _apply_style_to_elements(window, _get_accent_elements(window.ui), accent_style)
    window.ui.centralwidget.setStyleSheet(bg_style)
    clog('Установлена светлая тема')
def switchThemeToDark(window):
    if not window or not hasattr(window, 'ui') or not window.ui:
        clog("Предупреждение: не удалось применить тёмную тему")
        return

    common_style = 'background-color: rgb(12, 26, 57); color: white; border-radius: 5px;'
    accent_style = 'background-color: rgb(12, 26, 100); color: white; border-radius: 5px;'
    bg_style = 'background-color: rgb(12, 18, 31);'

    # Применяем стили
    _apply_style_to_elements(window, _get_common_elements(window.ui), common_style)
    _apply_style_to_elements(window, _get_accent_elements(window.ui), accent_style)
    window.ui.centralwidget.setStyleSheet(bg_style)
    window.ui.pushButton_8.setStyleSheet(accent_style)
    clog('Установлена тёмная тема')