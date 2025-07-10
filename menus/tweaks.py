from tweaks.context_menu import restore_win10_context_menu
def tweaksMenu():
    d = input('Выберите пункт:\n1. Включение старого контекстного меню(из windows 10)\n')
    if d == '1':
        restore_win10_context_menu()
    else:
        pass