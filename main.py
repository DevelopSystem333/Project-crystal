import ctypes
import sys
from menus.clean import cleanMenu
from menus.optimization import optimizationMenu
from menus.tweaks import tweaksMenu
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()
else:
    print("Скрипт запущен с правами администратора!")

while True:  # Бесконечный цикл для меню
    a = input('Выберите пункт:\n1. Очистка\n2. Оптимизация\n3. Твики\n4. Выход\n')  # Добавил пункт для выхода
    
    if a == '1':
        cleanMenu()
    elif a == '2':
        optimizationMenu()
    elif a == '3':
        tweaksMenu()
    elif a == '4':  # Добавил условие для выхода из программы
        print("Выход из программы...")
        break  # Выход из цикла
    else:
        print("Неверный выбор, попробуйте еще раз!")